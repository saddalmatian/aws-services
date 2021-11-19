from models.schemas import reaction as reaction_schema
from db import reaction as reaction_db

def add_issue_reaction(reaction:reaction_schema.IssueReactionIn):
    return reaction_db.add_issue_reaction(reaction)

def add_pullreq_reaction(reaction:reaction_schema.PullReqReactionIn):
    return reaction_db.add_pullreq_reaction(reaction) 

def add_issuecmt_reaction(reaction:reaction_schema.IssueCommentReactionIn):
    return reaction_db.add_issuecmt_reaction(reaction)

def add_pullreqcmt_reaction(reaction:reaction_schema.PullReqCommentReactionIn):
    return reaction_db.add_pullreqcmt_reaction(reaction)
