from fastapi import APIRouter
from typing import List
from models.schemas import repo as repo_schema
from services import repo as repo_service

router = APIRouter(
    prefix="/comment",
    tags=["Comment"]
)

@router.post("/")
def create_repo(repo:repo_schema.RepoIn):
    return repo_service.create_repo(repo)

@router.get("/",response_model=repo_schema.RepoResp)
def get_repo(repo_owner:str,repo_name:str):
    return repo_service.get_repo(repo_owner,repo_name)


