from pydantic import BaseModel
from typing import Dict, Set
from datetime import datetime
from models.domains import repo as repo_domains
from models.domains import reaction as reaction_domains
from pydantic.fields import Field


class IssueComment(BaseModel):
    commenter:str = Field(...,alias="Commenter")
    content:str = Field(...,alias="CommentContent")
    issue_number:int = Field(...,alias="IssueNumber")
    repo: repo_domains.Repo = Field(alias="Repo")

class IssueCommentInDB(BaseModel):
    commenter:str = Field(...,alias="Commenter")
    content:str = Field(...,alias="CommentContent")
    issue_number:int = Field(...,alias="IssueNumber")
    comment_id:str = Field(...,alias="CommentID")
    created_at:datetime = Field(...,alias="CreatedAt")
    reaction:dict = Field(...,alias="Reaction")

class PullReqComment(BaseModel):
    commenter:str = Field(...,alias="Commenter")
    content:str = Field(...,alias="CommentContent")
    pullreq_number:int = Field(...,alias="PullReqNumber")
    repo: repo_domains.Repo = Field(alias="Repo")

class PullReqCommentInDB(BaseModel):
    commenter:str = Field(...,alias="Commenter")
    content:str = Field(...,alias="CommentContent")
    pullreq_number:int = Field(...,alias="PullReqNumber")
    comment_id:str = Field(...,alias="CommentID")
    created_at:datetime = Field(...,alias="CreatedAt")
    reaction:dict = Field(...,alias="Reaction")