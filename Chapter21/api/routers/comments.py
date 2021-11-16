from fastapi import APIRouter
from typing import List
from models.schemas import comment as comment_schema
from services import comment as comment_service

router = APIRouter(
    prefix="/comment",
    tags=["Comments"]
)

@router.post("/issue")
def create_issue_comment(comment:comment_schema.IssueCommentIn):
    return comment_service.create_issue_comment(comment)

@router.get("/issue",response_model=List[comment_schema.IssueCommentResp])
def fetch_issue_comments(repo_owner:str,repo_name:str,issue_number:int): 
    return comment_service.fetch_issue_comments(repo_owner,repo_name,issue_number)

@router.post("/pull-request")
def create_pullreq_comment(comment:comment_schema.PullReqCommentIn):
    return comment_service.create_pullreq_comment(comment)

@router.get("/pull-request",response_model=List[comment_schema.PullReqCommentResp])
def fetch_pullreq_comments(repo_owner:str,repo_name:str,pullreq_number:int): 
    return comment_service.fetch_pullreq_comments(repo_owner,repo_name,pullreq_number)