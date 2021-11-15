from fastapi import APIRouter
from models.schemas import repo as repo_schema
from services import repo as repo_service

router = APIRouter(
    prefix="/repo",
    tags=["Repository"]
)

@router.post("/")
def create_repo(repo:repo_schema.RepoIn):
    return repo_service.create_repo(repo)

@router.get("/",response_model=repo_schema.RepoResp)
def get_repo(repo_owner:str,repo_name:str):
    return repo_service.get_repo(repo_owner,repo_name)

@router.post("/issue/")
def create_repo_issue(issue:repo_schema.IssueIn):
    return repo_service.create_repo_issuse(issue) 

@router.post("/pull-request/")
def create_repo_pullreq(pullreq:repo_schema.PullReqIn):
    return repo_service.create_repo_pullreq(pullreq) 

@router.get("/fetch-issue")
def fetch_repo_issues(repo_owner:str,repo_name:str):
    return repo_service.fetch_repo_issues(repo_owner,repo_name)

@router.get("/issue")
def get_repo_issue(repo_owner:str,repo_name:str,issue_number:int):
    return repo_service.get_repo_issue(repo_owner,repo_name,issue_number)

@router.get("/fetch-pullreq")
def fetch_repo_pullreqs(repo_owner:str,repo_name:str):
    return repo_service.fetch_repo_pullreqs(repo_owner,repo_name)

@router.get("/pull-request")
def get_repo_pullreq(repo_owner:str,repo_name:str,pullreq_number:int):
    return repo_service.get_repo_pullreq(repo_owner,repo_name,pullreq_number)

@router.get("/open-status")
def fetch_open_status(repo_owner:str,repo_name:str):
    return repo_service.fetch_open_status(repo_owner,repo_name)

@router.post("/fork")
def create_fork(fork:repo_schema.ForkIn):
    return repo_service.create_fork(fork) 