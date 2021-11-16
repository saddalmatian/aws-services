from pydantic import BaseModel
from datetime import datetime
from models.domains import repo as repo_domains
from pydantic.fields import Field

class IssueComment(BaseModel):
    commenter:str = Field(...,alias="Commenter")
    content:str = Field(...,alias="Content")
    issue_number:int = Field(...,alias="IssueNumber")
    repo: repo_domains.Repo = Field(alias="Repo")

class IssueCommentInDB(IssueComment):
    comment_id:str = Field(...,alias="CommentID")
    created_at:datetime = Field(...,alias="CreatedAt")