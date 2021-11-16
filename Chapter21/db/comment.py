from models.schemas import comment as comment_schema
from db.utils import table
from datetime import datetime
from boto3.dynamodb.conditions import Key
from ksuid import Ksuid

def create_issue_comment(comment:comment_schema.IssueCommentIn):
    ksuid = Ksuid()
    response = table.put_item(
        Item={
            "PK":"ISSUECOMMENT#"+comment.repo.repo_owner+"#"+comment.repo.repo_name+"#"+str(comment.issue_number),
            "SK":"ISSUECOMMENT#"+str(ksuid),
            "CreatedAt":ksuid.datetime.strftime("%Y-%m-%d %H:%M"),
            "IssueNumber":comment.issue_number,
            "CommentID":str(ksuid),
            "Commenter":comment.commenter,
            "CommentContent":comment.content
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response

def fetch_issue_comments(repo_owner:str,repo_name:str,issue_number:int):
    response = table.query(
        KeyConditionExpression=Key("PK").eq("ISSUECOMMENT#"+repo_owner+"#"+repo_name+"#"+str(issue_number))
    )
    return response["Items"]

def create_pullreq_comment(comment:comment_schema.PullReqCommentIn):
    ksuid = Ksuid()
    response = table.put_item(
        Item={
            "PK":"PRCOMMENT#"+comment.repo.repo_owner+"#"+comment.repo.repo_name+"#"+str(comment.pullreq_number),
            "SK":"PRCOMMENT#"+str(ksuid),
            "CreatedAt":ksuid.datetime.strftime("%Y-%m-%d %H:%M"),
            "PullReqNumber":comment.pullreq_number,
            "CommentID":str(ksuid),
            "Commenter":comment.commenter,
            "CommentContent":comment.content
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response

def fetch_pullreq_comments(repo_owner:str,repo_name:str,pullreq_number:int):
    response = table.query(
        KeyConditionExpression=Key("PK").eq("PRCOMMENT#"+repo_owner+"#"+repo_name+"#"+str(pullreq_number))
    )
    return response["Items"]