import requests
import json
import environment_variables as env

class GithubAPI:
    def __init__(self, pr_url:str):
        self.base_url = "https://api.github.com/repos"       
        if "https://github.com" in pr_url:
            self.pr_url = pr_url.replace(
                "https://github.com",
                self.base_url
            ).replace("/pull/","/pulls/")
        elif self.base_url in pr_url:
            self.pr_url = pr_url
        else:
            raise Exception(
                f"Provided Pull request url '{pr_url}' is not valid, please provide a valid url"
            )
        self.pr_data = self._get_pr_data()
        self.diff_url = self.pr_data["diff_url"]
        self.review_url = self.pr_data["review_comments_url"].replace("/comments", "/reviews")
        self.diff_data = self._get_diff_data()

    def _get_pr_data(self) -> dict:
        try:
            response = requests.get(
                self.pr_url,
                headers=env.GITHUB_HEADERS
            )
            response.raise_for_status()
            return json.loads(response.text)
        
        except Exception as e:
            print(f"Something went wrong getting PR Data from {self.pr_url}: {e}")

    def _get_diff_data(self) -> str:
        try:
            response = requests.get(
                self.diff_url,
                headers=env.GITHUB_HEADERS
            )
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Something went wrong getting diff Data from {self.pr_url}: {e}")

    def send_pr_review(self, json_body:dict) -> str:
        json_body["commit_id"] = self.pr_data["head"]["sha"]
        try:
            response = requests.post(
                self.review_url,
                headers=env.GITHUB_HEADERS,
                json=json_body
            )
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Something went wrong adding comments to {self.pr_url}: {e}")
