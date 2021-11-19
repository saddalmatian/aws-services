from fastapi import APIRouter
from typing import List
from models.schemas import reaction as reaction_schema
from services import reaction as reaction_service

router = APIRouter(
    prefix="/reaction",
    tags=["Reactions"] 
)
@router.put("/issue") 
def add_issue_reaction(reaction: reaction_schema.IssueReactionIn):
    return reaction_service.add_issue_reaction(reaction)

@router.put("/pull-req") 
def add_pullreq_reaction(reaction: reaction_schema.PullReqReactionIn):
    return reaction_service.add_pullreq_reaction(reaction)
 
@router.put("/issue-comment") 
def add_issuecmt_reaction(reaction: reaction_schema.IssueCommentReactionIn):
    return reaction_service.add_issuecmt_reaction(reaction)
 
@router.put("/pull-req-comment")
def add_pullreqcmt_reaction(reaction: reaction_schema.PullReqCommentReactionIn):
    return reaction_service.add_pullreqcmt_reaction(reaction)