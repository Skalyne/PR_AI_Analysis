import unittest
from unittest.mock import patch
import requests

# Assuming the code you provided is in a file named github_api.py
from github_api import GithubAPI 

class TestGithubAPI(unittest.TestCase):

    @patch('github_api.GithubAPI._get_pr_data')
    @patch('github_api.GithubAPI._get_diff_data')
    def test_init_valid_github_url(self, mock_get_diff_data, mock_get_pr_data):
        mock_get_pr_data.return_value = {
            "diff_url": "https://api.github.com/repos/owner/repo/pulls/1.diff",
            "review_comments_url": "https://api.github.com/repos/owner/repo/pulls/1/comments"
        }
        mock_get_diff_data.return_value = "some diff data"
        
        pr_url = "https://github.com/owner/repo/pull/1"
        api = GithubAPI(pr_url)
        self.assertEqual(api.pr_url, "https://api.github.com/repos/owner/repo/pulls/1")
        self.assertEqual(api.diff_url, "https://api.github.com/repos/owner/repo/pulls/1.diff")
        self.assertEqual(api.review_url, "https://api.github.com/repos/owner/repo/pulls/1/reviews")

    @patch('github_api.GithubAPI._get_pr_data')
    @patch('github_api.GithubAPI._get_diff_data')
    def test_init_valid_api_url(self, mock_get_diff_data, mock_get_pr_data):
        mock_get_pr_data.return_value = {
            "diff_url": "https://api.github.com/repos/owner/repo/pulls/1.diff",
            "review_comments_url": "https://api.github.com/repos/owner/repo/pulls/1/comments"
        }
        mock_get_diff_data.return_value = "some diff data"

        pr_url = "https://api.github.com/repos/owner/repo/pulls/1"
        api = GithubAPI(pr_url)
        self.assertEqual(api.pr_url, "https://api.github.com/repos/owner/repo/pulls/1")
        self.assertEqual(api.diff_url, "https://api.github.com/repos/owner/repo/pulls/1.diff")
        self.assertEqual(api.review_url, "https://api.github.com/repos/owner/repo/pulls/1/reviews")

    @patch('github_api.GithubAPI._get_pr_data')
    @patch('github_api.GithubAPI._get_diff_data')
    def test_init_invalid_url(self, mock_get_diff_data, mock_get_pr_data):
        pr_url = "https://someotherdomain.com/owner/repo/pull/1"
        with self.assertRaisesRegex(Exception, "Provided Pull request url '.*' is not valid"):
            GithubAPI(pr_url)

if __name__ == '__main__':
    unittest.main()