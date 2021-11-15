from models.domains import repo


class RepoIn(repo.Repo):
    pass

class RepoResp(repo.RepoInDB):
    pass

class IssueIn(repo.Issue):
    pass

class PullReqIn(repo.PullReq):
    pass

class ForkIn(repo.Fork):
    pass