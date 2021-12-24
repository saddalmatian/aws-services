from models.schemas import comment as comment_schemas
from db import comment as comment_db

def create_issue_comment(comment:comment_schemas.IssueCommentIn):
    return comment_db.create_issue_comment(comment)

def fetch_issue_comments(repo_owner:str,repo_name:str,issue_number:int):
    return comment_db.fetch_issue_comments(repo_owner,repo_name,issue_number)

def create_pullreq_comment(comment:comment_schemas.PullReqCommentIn):
    return comment_db.create_pullreq_comment(comment)

def fetch_pullreq_comments(repo_owner:str,repo_name:str,pullreq_number:int):
    return comment_db.fetch_pullreq_comments(repo_owner,repo_name,pullreq_number)