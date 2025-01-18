import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

GITHUB_HEADERS = {
    'Authorization': f'Bearer {GITHUB_TOKEN}',
    'content-type': 'application/json',
}
