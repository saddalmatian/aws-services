from models.schemas import repo as repo_schema
from db.utils import table
from datetime import datetime
from boto3.dynamodb.conditions import Key

def create_repo(repo:repo_schema.RepoIn):
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = table.put_item(
        Item={
            "PK":"REPO#"+repo.repo_owner+"#"+repo.repo_name,
            "SK":"REPO#"+repo.repo_owner+"#"+repo.repo_name,
            "RepoOwner":repo.repo_owner,
            "RepoName":repo.repo_name,
            "IssueAndPullCount":0,
            "StarCount":0,
            "ForkCount":0,
            "CreatedAt":created_at,
            "GSI1PK":"REPO#"+repo.repo_owner+"#"+repo.repo_name,
            "GSI1SK":"REPO#"+repo.repo_owner+"#"+repo.repo_name,
            "GSI2PK":"REPO#"+repo.repo_owner+"#"+repo.repo_name,
            "GSI2SK":"#REPO#"+repo.repo_name
        },
        ConditionExpression="attribute_not_exists(PK)"
    )

    return response

def create_repo_issue(issue:repo_schema.IssueIn):
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resp = table.update_item(
        Key={
             "PK":"REPO#"+issue.repo.repo_owner+"#"+issue.repo.repo_name,
            "SK":"REPO#"+issue.repo.repo_owner+"#"+issue.repo.repo_name,
        },
        UpdateExpression="SET IssueAndPullCount = IssueAndPullCount + :ic",
        ExpressionAttributeValues={
            ":ic":1
        },
        ReturnValues="UPDATED_NEW"
    )
    zero_padded_issue = f'{resp["Attributes"]["IssueAndPullCount"]:07}'

    response = table.put_item(
        Item={
            "PK":"REPO#"+issue.repo.repo_owner+"#"+issue.repo.repo_name,
            "SK":"ISSUE#"+zero_padded_issue,
            "RepoName":issue.repo.repo_name,
            "RepoOwner":issue.repo.repo_owner,
            "CreatedAt":created_at,
            "IssueNumber":resp["Attributes"]["IssueAndPullCount"],
            "Status":"Open",
        },
        ConditionExpression="attribute_not_exists(PK)"
    )

    return response

def create_repo_pullreq(pullreq:repo_schema.PullReqIn):
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resp = table.update_item(
        Key={
            "PK":"REPO#"+pullreq.repo.repo_owner+"#"+pullreq.repo.repo_name,
            "SK":"REPO#"+pullreq.repo.repo_owner+"#"+pullreq.repo.repo_name,
        },
        UpdateExpression="SET IssueAndPullCount = IssueAndPullCount + :ic",
        ExpressionAttributeValues={
            ":ic":1
        },
        ReturnValues="UPDATED_NEW"
    )
    zero_padded_pullreq = f'{resp["Attributes"]["IssueAndPullCount"]:07}'

    response = table.put_item(
        Item={
            "PK":"PR#"+pullreq.repo.repo_owner+"#"+pullreq.repo.repo_name+"#"+zero_padded_pullreq,
            "SK":"PR#"+pullreq.repo.repo_owner+"#"+pullreq.repo.repo_name+"#"+zero_padded_pullreq,
            "RepoName":pullreq.repo.repo_name,
            "RepoOwner":pullreq.repo.repo_owner,
            "CreatedAt":created_at,
            "PullRequestNumber":resp["Attributes"]["IssueAndPullCount"],
            "GSI1PK":"REPO#"+pullreq.repo.repo_owner+"#"+pullreq.repo.repo_name,
            "GSI1SK":"PR#"+zero_padded_pullreq
        },
        ConditionExpression="attribute_not_exists(PK)"
    )

    return response    

def get_repo(repo_owner:str,repo_name:str):
    response = table.get_item(
        Key={
            "PK":"REPO#"+repo_owner+"#"+repo_name,
            "SK":"REPO#"+repo_owner+"#"+repo_name
        }
    )
    return response["Item"]

def fetch_repo_issues(repo_owner:str,repo_name:str):
    response = table.query(
        KeyConditionExpression=Key("PK").eq("REPO#"+repo_owner+"#"+repo_name) & Key("SK").begins_with("ISSUE#"),
        ProjectionExpression="RepoOwner,IssueNumber,RepoName,CreatedAt,#stt",
        ExpressionAttributeNames={
            "#stt":"Status"
        }
    )
    return response["Items"]

def fetch_repo_pullreqs(repo_owner:str,repo_name:str):
    response = table.query(
        IndexName="GSI1",
        KeyConditionExpression=Key("GSI1PK").eq("REPO#"+repo_owner+"#"+repo_name) & Key("GSI1SK").begins_with("PR#"),
        ProjectionExpression="RepoOwner,PullRequestNumber,RepoName,CreatedAt",
    )
    return response["Items"]

def get_repo_issue(repo_owner:str,repo_name:str,issue_number:int):
    zero_padded_issue = f'{issue_number:07}'
    response = table.get_item(
        Key={
            "PK":"REPO#"+repo_owner+"#"+repo_name,
            "SK":"ISSUE#"+zero_padded_issue
        },
        ProjectionExpression="RepoOwner,IssueNumber,RepoName,CreatedAt,#stt",
        ExpressionAttributeNames={
            "#stt":"Status"
        }
    )
    return response["Item"]

def get_repo_pullreq(repo_owner:str,repo_name:str,pullreq_number:int):
    zero_padded_pullreq = f'{pullreq_number:07}'
    response = table.get_item(
        Key={
            "PK":"PR#"+repo_owner+"#"+repo_name+"#"+zero_padded_pullreq,
            "SK":"PR#"+repo_owner+"#"+repo_name+"#"+zero_padded_pullreq
        },
        ProjectionExpression="RepoOwner,PullRequestNumber,RepoName,CreatedAt",
    )
    print("PR#"+repo_owner+"#"+repo_name+zero_padded_pullreq)
    return response["Item"]

def fetch_open_status(repo_owner:str,repo_name:str):
    response = table.query(
        KeyConditionExpression=Key("PK").eq("REPO#"+repo_owner+"#"+repo_name),
        FilterExpression="attribute_not_exists(#status) OR #status = :status",
        ExpressionAttributeNames={
            "#status": "Status"
        },
        ExpressionAttributeValues={
            ":status":"Open"
        },
        ScanIndexForward=False
    )
    return response["Items"]

def create_fork(fork:repo_schema.ForkIn):
    table.update_item(
        Key={
            "PK":"REPO#"+fork.repo_owner+"#"+fork.repo_name,
            "SK":"REPO#"+fork.repo_owner+"#"+fork.repo_name,
        },
        UpdateExpression="SET ForkCount = ForkCount + :fc",
        ExpressionAttributeValues={
            ":fc":1
        }
    )
    response =  table.put_item(
        Item={
            "PK":"REPO#"+fork.repo_owner+"#"+fork.repo_name,
            "SK":"REPO#"+fork.repo_owner+"#"+fork.repo_name,
            "RepoOwner":fork.repo_owner,
            "RepoName":fork.repo_name,
            "GSI2PK":"REPO#"+fork.repo_original_owner+"#"+fork.repo_name,
            "GSI2SK":"FORK#"+fork.repo_owner
        },
        ConditionExpression="attribute_not_exists(PK)",
    )
    return response

def fetch_forks(repo_owner:str,repo_name:str):
    response = table.query(
        IndexName="GSI2",
        KeyConditionExpression=Key("GSI2PK").eq("REPO#"+repo_owner+"#"+repo_name) & Key("GSI2SK").begins_with("FORK#")
    )
    return response["Items"]

def create_star(star:repo_schema.StarIn):
    table.update_item(
        Key={
            "PK":"REPO#"+star.repo_owner+"#"+star.repo_name,
            "SK":"REPO#"+star.repo_owner+"#"+star.repo_name,
        },
        UpdateExpression="SET StarCount = StarCount + :sc",
        ExpressionAttributeValues={
            ":sc":1
        }
    )
    
    response =  table.put_item(
        Item={
            "PK":"REPO#"+star.repo.repo_owner+"#"+star.repo.repo_name,
            "SK":"Star#"+star.starring_user,
            "StarringUser":star.starring_user
        },
        ConditionExpression="attribute_not_exists(PK)",
    )
    return response

def fetch_stars(repo_owner:str,repo_name:str):
    response = table.query(
        KeyConditionExpression=Key("PK").eq("REPO#"+repo_owner+"#"+repo_name) & Key("SK").gt("REPO#"),
        ProjectionExpression="RepoOwner,RepoName,IssueAndPullCount,CreatedAt,StarringUser"
    )
    
    return response["Items"]