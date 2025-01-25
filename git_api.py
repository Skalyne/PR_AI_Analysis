from github import Github, Auth
from environment_variables import GITHUB_TOKEN


class GitHubApi:
    def __init__(self, repo_name=None):
        self.repo_name = repo_name
        auth = Auth.Token(GITHUB_TOKEN)
        self.github_instance = Github(auth=auth)

    def manage_pull_request(self):
        repo = self.github_instance.get_repo(self.repo_name)

if __name__ == "__main__":
    g = GitHubApi("PR_AI_Analysis")
    g.manage_pull_request()


        