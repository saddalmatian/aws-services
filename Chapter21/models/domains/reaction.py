from pydantic import BaseModel
from datetime import datetime
from pydantic.fields import Field
from models.domains import repo

repository = repo.Repo

class IssueReaction(BaseModel):
    issue_number:int = Field(...,alias="IssueNumber")
    repo:repository = Field(...,alias="Repo")
    user:str = Field(...,alias="User")
    reaction: str = Field(...,alias="Reaction")

class PullReqReaction(BaseModel):
    pullreq_number:int = Field(...,alias="PullReqNumber")
    repo:repository = Field(...,alias="Repo")
    user:str = Field(...,alias="User")
    reaction: str = Field(...,alias="Reaction")

class IssueCommentReaction(BaseModel):
    issue_number:int = Field(...,alias="IssueNumber")
    comment_id:str = Field(...,alias="CommentID")
    repo:repository = Field(...,alias="Repo")
    user:str = Field(...,alias="User")
    reaction: str = Field(...,alias="Reaction")

class PullReqCommentReaction(BaseModel):
    pullreq_number:int = Field(...,alias="PullReqNumber")
    comment_id:str = Field(...,alias="CommentID")
    repo:repository = Field(...,alias="Repo")
    user:str = Field(...,alias="User")
    reaction: str = Field(...,alias="Reaction")