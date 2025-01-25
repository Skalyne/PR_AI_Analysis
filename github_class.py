from github import Github, GithubException, Auth
from environment_variables import GITHUB_TOKEN

class PRDiff:
    """
    A class to retrieve the diff of a specific pull request using the PyGithub library.
    """

    def __init__(self, repo_name):
        """
        Initializes the PRDiff object.

        Args:
            repo_name (str): The full name of the repository (e.g., "user/repo").
        """
        self.repo_name = repo_name
        auth = Auth.Token(GITHUB_TOKEN)
        self.github = Github(auth=auth)

        try:
            self.repo = self.github.get_repo(repo_name)
        except GithubException as e:
            raise ValueError(f"Error accessing repository '{repo_name}': {e}")

    def get_diff(self, pr_number):
        """
        Retrieves the diff of a specific pull request.

        Args:
            pr_number (int): The number of the pull request.

        Returns:
            str: The diff of the pull request, or None if an error occurred.
        """
        try:
            pr = self.repo.get_pull(pr_number)

            # PyGithub doesn't directly provide the diff content,
            # so we need to fetch it separately using requests.
            print("x")
        except GithubException as e:
            print(f"Error getting PR #{pr_number}: {e}")
            return None

    def get_diff_by_commit(self, commit_sha):
        """
        Retrieves the diff for a specific commit.

        Args:
            commit_sha (str): The SHA of the commit.

        Returns:
            str: The diff of the commit, or None if an error occurred.
        """

        try:
            commit = self.repo.get_commit(commit_sha)
            if len(commit.parents) > 1:
              print(f"Commit {commit_sha} is a merge commit. Returning combined diff.")

            diffs = []
            for file in commit.files:
              diffs.append(file.patch)

            return "\n".join(diffs)
        except GithubException as e:
            print(f"Error getting commit {commit_sha}: {e}")
            return None

# Example Usage
if __name__ == "__main__":
    g = PRDiff("Skalyne/PR_AI_Analysis")
    g.get_diff(7)
    g.github.close()