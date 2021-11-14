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
def get_repo(repo_name:str,repo_owner:str):
    return repo_service.get_repo(repo_name,repo_owner)

@router.post("/issue/")
def create_repo_issue(issue:repo_schema.IssueIn):
    return repo_service.create_repo_issuse(issue) 