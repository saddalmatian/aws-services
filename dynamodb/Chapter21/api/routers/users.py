from fastapi import APIRouter, Depends
from typing import List
from db.login import validate_token, oauth2_scheme
from models.schemas import user as user_schema
from models.schemas import repo as repo_schema
from services import user as user_service

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("/user")
def create_user(user: user_schema.UserIn):
    return user_service.create_user(user)


@router.get("/user",
            response_model=user_schema.UserResp,
            dependencies=[Depends(validate_token)]
            )
def get_user(username: str, token=Depends(oauth2_scheme)):
    return user_service.get_user(username)


@router.get("/user-org")
def get_user_org(username: str):
    return user_service.get_user_org(username)


@router.post("/organization")
def create_org(org: user_schema.OrgIn):
    return user_service.create_org(org)


@router.get("/organization", response_model=user_schema.OrgResp)
def get_org(orgname: str):
    return user_service.get_org(orgname)


@router.post("/user-org")
def add_user_org(username: str, orgname: str):
    return user_service.add_user_org(username, orgname)


@router.get("/user-repo", response_model=List[repo_schema.RepoResp])
def get_user_repo(username: str):
    return user_service.get_user_repo(username)


@router.get("/org-repo", response_model=List[repo_schema.RepoResp])
def get_org_repo(orgname: str):
    return user_service.get_org_repo(orgname)
