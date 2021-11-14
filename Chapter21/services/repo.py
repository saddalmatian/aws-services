from models.schemas import repo as repo_schema
from db import repo as repo_db


def create_repo(repo:repo_schema.RepoIn):
    return repo_db.create_repo(repo)

def get_repo(repo_name:str,repo_owner:str):
    return repo_db.get_repo(repo_name,repo_owner)

def create_repo_issuse(issue:repo_schema.IssueIn):
    return repo_db.create_repo_issue(issue) 