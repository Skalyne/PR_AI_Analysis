from pr_analysis import DiffAnalysis
from pr_data import PullRequestData

pr_url = "https://api.github.com/repos/Skalyne/PR_AI_Analysis/pulls/3"

pr_data = PullRequestData(pr_url)
diff = pr_data.get_pr_diff()

analysis = DiffAnalysis(diff)
generate = analysis.generate_response()

for item in generate:
    comment = pr_data.make_comments(item)
