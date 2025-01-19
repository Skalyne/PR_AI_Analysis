import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

GITHUB_HEADERS = {
    'Authorization': f'Bearer {GITHUB_TOKEN}',
    'content-type': 'application/json',
}

GOOGLE_AI_TOKEN = os.getenv("GOOGLE_AI_TOKEN")
