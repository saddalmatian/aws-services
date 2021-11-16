from models.domains import comment

class IssueCommentIn(comment.IssueComment):
    pass

class IssueCommentResp(comment.IssueCommentInDB):
    pass

class PullReqCommentIn(comment.PullReqComment):
    pass

class PullReqCommentResp(comment.PullReqCommentInDB):
    pass