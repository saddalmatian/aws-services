from models.schemas import reaction as reaction_schema
from db.utils import table
from datetime import datetime
from boto3.dynamodb.conditions import Key

def add_issue_reaction(reaction:reaction_schema.IssueReactionIn):
    response = table.update_item(
        Key={
            "PK":"ISSUEREACTION#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+str(reaction.issue_number)+"#"+reaction.user,
            "SK":"ISSUEREACTION#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+str(reaction.issue_number)+"#"+reaction.user,
        },
        UpdateExpression="ADD Reactions :reaction",
        ConditionExpression="attribute_not_exists(Reactions)",
        ExpressionAttributeValues={
            ":reaction": {reaction.reaction}
        }
    )
    
    zero_padded_issue = f'{reaction.issue_number:07}'
    response = table.update_item(
        Key={
            "PK":"REPO#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name,
            "SK":"ISSUE#"+str(zero_padded_issue)
        },
        UpdateExpression="SET Reaction.#reaction = Reaction.#reaction + :count",
        ExpressionAttributeNames={
            "#reaction":reaction.reaction
        },
        ExpressionAttributeValues={
            ":count":1
        }
    )
    return response

def add_pullreq_reaction(reaction:reaction_schema.PullReqReactionIn):
    response = table.update_item(
        Key={
            "PK":"PRREACTION#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+str(reaction.pullreq_number)+"#"+reaction.user,
            "SK":"PRREACTION#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+str(reaction.pullreq_number)+"#"+reaction.user,
        },
        UpdateExpression="ADD Reactions :reaction",
        ConditionExpression="attribute_not_exists(Reactions)",
        ExpressionAttributeValues={
            ":reaction": {reaction.reaction}
        }
    )
    
    zero_padded_pullreq = f'{reaction.pullreq_number:07}'
    response = table.update_item(
        Key={
            "PK":"PR#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+zero_padded_pullreq,
            "SK":"PR#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+zero_padded_pullreq
        },
        UpdateExpression="SET Reaction.#reaction = Reaction.#reaction + :count",
        ExpressionAttributeNames={
            "#reaction":reaction.reaction
        },
        ExpressionAttributeValues={
            ":count":1
        }
    )
    return response

def add_issuecmt_reaction(reaction:reaction_schema.IssueCommentReactionIn):
    response = table.update_item(
        Key={
            "PK":"ISSUEREACTION#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+str(reaction.issue_number)+"#"+reaction.user+"#"+reaction.comment_id,
            "SK":"ISSUEREACTION#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+str(reaction.issue_number)+"#"+reaction.user+"#"+reaction.comment_id,
        },
        UpdateExpression="ADD Reactions :reaction",
        ConditionExpression="attribute_not_exists(Reactions)",
        ExpressionAttributeValues={
            ":reaction": {reaction.reaction}
        }
    )
    
    zero_padded_issue = f'{reaction.issue_number:07}'
    response = table.update_item(
        Key={
            "PK":"ISSUECOMMENT#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+str(reaction.issue_number),
            "SK":"ISSUECOMMENT#"+reaction.comment_id
        },
        UpdateExpression="SET Reaction.#reaction = Reaction.#reaction + :count",
        ExpressionAttributeNames={
            "#reaction":reaction.reaction
        },
        ExpressionAttributeValues={
            ":count":1
        }
    )
    return response

def add_pullreqcmt_reaction(reaction:reaction_schema.PullReqCommentReactionIn):
    response = table.update_item(
        Key={
            "PK":"PRREACTION#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+str(reaction.pullreq_number)+"#"+reaction.user+"#"+reaction.comment_id,
            "SK":"PRREACTION#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+str(reaction.pullreq_number)+"#"+reaction.user+"#"+reaction.comment_id,
        },
        UpdateExpression="ADD Reactions :reaction",
        ConditionExpression="attribute_not_exists(Reactions)",
        ExpressionAttributeValues={
            ":reaction": {reaction.reaction}
        }
    )
    response = table.update_item(
        Key={
            "PK":"PRCOMMENT#"+reaction.repo.repo_owner+"#"+reaction.repo.repo_name+"#"+str(reaction.pullreq_number),
            "SK":"PRCOMMENT#"+reaction.comment_id
        },
        UpdateExpression="SET Reaction.#reaction = Reaction.#reaction + :count",
        ExpressionAttributeNames={
            "#reaction":reaction.reaction
        },
        ExpressionAttributeValues={
            ":count":1
        }
    )
    
    return response