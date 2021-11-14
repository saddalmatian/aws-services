from pydantic import BaseModel
from datetime import datetime
from pydantic.fields import Field


class Repo(BaseModel):
    repo_owner: str = Field(...,alias="RepoOwner")
    repo_name: str = Field(...,alias="RepoName")

class RepoInDB(Repo):
    created_at:datetime = Field(...,alias="CreatedAt")

class Issue(BaseModel):
    repo: Repo = Field(...,alias="Repo")
    issue_number:str = Field(...,alias="IssueNumber")
    
class IssueInDB(Issue):
    created_at:datetime = Field(...,alias="CreatedAt")
    status:str = Field(...,alias="Status")