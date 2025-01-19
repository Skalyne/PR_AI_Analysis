from pr_analysis import DiffAnalysis
from github_api import GithubAPI

pr_url = "https://api.github.com/repos/Skalyne/PR_AI_Analysis/pulls/3"

pr_data = GithubAPI(pr_url)
diff = pr_data.diff_data

analysis = DiffAnalysis(diff)
generate = analysis.generate_response()

for item in generate:
    comment = pr_data.send_pr_review(item)
