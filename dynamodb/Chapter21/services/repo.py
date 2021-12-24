from models.schemas import repo as repo_schema
from db import repo as repo_db


def create_repo(repo:repo_schema.RepoIn):
    return repo_db.create_repo(repo)

def get_repo(repo_owner:str,repo_name:str):
    return repo_db.get_repo(repo_owner,repo_name)

def create_repo_issuse(issue:repo_schema.IssueIn):
    return repo_db.create_repo_issue(issue) 

def create_repo_pullreq(pullreq:repo_schema.PullReqIn):
    return repo_db.create_repo_pullreq(pullreq)

def fetch_repo_issues(repo_owner:str,repo_name:str):
    return repo_db.fetch_repo_issues(repo_owner,repo_name)

def get_repo_issue(repo_owner:str,repo_name:str,issue_number:int):
    return repo_db.get_repo_issue(repo_owner,repo_name,issue_number)

def fetch_repo_pullreqs(repo_owner:str,repo_name:str):
    return repo_db.fetch_repo_pullreqs(repo_owner,repo_name)

def get_repo_pullreq(repo_owner:str,repo_name:str,pullreq_number:int):
    return repo_db.get_repo_pullreq(repo_owner,repo_name,pullreq_number)

def fetch_open_status(repo_owner:str,repo_name:str):
    return repo_db.fetch_open_status(repo_owner,repo_name)

def create_fork(fork:repo_schema.ForkIn):
    return repo_db.create_fork(fork)

def fetch_forks(repo_owner:str,repo_name:str):
    return repo_db.fetch_forks(repo_owner,repo_name)
 
def create_star(star:repo_schema.StarIn):
    return repo_db.create_star(star)

def fetch_stars(repo_owner:str,repo_name:str):
    response = repo_db.fetch_stars(repo_owner,repo_name)
    starring_list = []
    for i in range(1,len(response)):   
        starring_list.append(response[i]["StarringUser"])

    true_response = {
        "Repo":response[0]
    }
    true_response["StarringUser"]=starring_list
    return true_response