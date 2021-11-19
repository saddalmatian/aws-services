from models.domains import reaction

class IssueReactionIn(reaction.IssueReaction):
    pass

class PullReqReactionIn(reaction.PullReqReaction):
    pass

class IssueCommentReactionIn(reaction.IssueCommentReaction):
    pass

class PullReqCommentReactionIn(reaction.PullReqCommentReaction):
    pass
