from typing import Set
from pydantic import BaseModel
from datetime import datetime
from pydantic.fields import Field


class Repo(BaseModel):
    repo_owner: str = Field(...,alias="RepoOwner")
    repo_name: str = Field(...,alias="RepoName")

class RepoInDB(Repo):
    created_at:datetime = Field(...,alias="CreatedAt")
    issue_pull_count:int = Field(...,alias="IssueAndPullCount")

class Issue(BaseModel):
    repo: Repo = Field(...,alias="Repo")

class IssueInDB(Issue):
    created_at:datetime = Field(...,alias="CreatedAt")
    issue_number:int = Field(...,alias="IssueNumber")
    reaction:Set = Field(...,alias="Reaction")
    status:str = Field(...,alias="Status")

class PullReq(BaseModel):
    repo: Repo = Field(...,alias="Repo")

class PullReqInDB(PullReq):
    pullreq_number:int = Field(...,alias="PullRequestNumber")
    created_at:datetime = Field(...,alias="CreatedAt")
    reaction:Set = Field(...,alias="Reaction")

class ForkInDB(BaseModel):
    repo_owner:str=Field(...,alias="RepoOwner")
    repo_name:str=Field(...,alias="RepoName")  

class ForkIn(ForkInDB):
    repo_original_owner:str=Field(...,alias="RepoOriginalOwner")

class Star(BaseModel):
    repo: Repo = Field(...,alias="Repo")
    starring_user:str = Field(...,alias="StarringUser")