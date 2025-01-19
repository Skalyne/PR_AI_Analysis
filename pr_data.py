import requests, json
from environmet_variables import GITHUB_HEADERS

class PullRequestData:
    def __init__(self, pr_url):
        self.pr_url = pr_url
        self.pr_data = None
        
    def get_pr_diff(self):
        response = requests.get(self.pr_url, headers=GITHUB_HEADERS)
        response.raise_for_status()
        self.pr_data = json.loads(response.text)
        diff = self._get_pr_diff_data(self.pr_data["diff_url"])
        
        return diff

    def _get_pr_diff_data(self, diff_url):
        response = requests.get(diff_url, headers=GITHUB_HEADERS)
        response.raise_for_status()
        return response.text
    
    def make_comments(self, json_body):
        comments_url = str(self.pr_data["review_comments_url"]).replace("/comments", "/reviews")
        json_body["commit_id"] = self.pr_data["merge_commit_sha"]

        resposne = requests.post(comments_url, headers=GITHUB_HEADERS, json=json_body)
        resposne.raise_for_status()
        return resposne.text

   
# if __name__ == "__main__":
#     print(GITHUB_HEADERS)
#     pr_url = "https://api.github.com/repos/Skalyne/PR_AI_Analysis/pulls/1"
#     data = PullRequestData(pr_url)
#     data.get_pr_diff()