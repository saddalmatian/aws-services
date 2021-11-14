from models.schemas import repo as repo_schema
from db.utils import table
from datetime import datetime

def create_repo(repo:repo_schema.RepoIn):
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = table.put_item(
        Item={
            "PK":"REPO#"+repo.repo_owner+"#"+repo.repo_name,
            "SK":"REPO#"+repo.repo_owner+"#"+repo.repo_name,
            "RepoOwner":repo.repo_owner,
            "RepoName":repo.repo_name,
            "CreatedAt":created_at,
        },
        ConditionExpression="attribute_not_exists(PK)"
    )

    return response

def create_repo_issue(issue:repo_schema.IssueIn):
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    zero_padded_issue = f'{issue.issue_number:07}'
    response = table.put_item(
        Item={
            "PK":"REPO#"+issue.repo.repo_owner+"#"+issue.repo.repo_name,
            "SK":"ISSUE#"+zero_padded_issue+"",
            "RepoName":issue.repo.repo_name,
            "RepoOwner":issue.repo.repo_owner,
            "CreatedAt":created_at,
            "IssueNumber":issue.issue_number,
            "Status":"Open"
        },
        ConditionExpression="attribute_not_exists(PK)"
    )

    return response

def get_repo(repo_name:str,repo_owner:str):
    response = table.get_item(
        Key={
            "PK":"REPO#"+repo_owner+"#"+repo_name,
            "SK":"REPO#"+repo_owner+"#"+repo_name
        }
    )
    return response["Item"]
