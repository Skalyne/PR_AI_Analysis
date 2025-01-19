# PR AI Analysis

[![GitHub Actions Status](https://github.com/Skalyne/PR_AI_Analysis/workflows/CI/badge.svg)](https://github.com/Skalyne/PR_AI_Analysis/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

**PR AI Analysis** is a project that utilizes the power of Large Language Models (LLMs) to analyze GitHub Pull Requests. It aims to automate and enhance the code review process, helping developers merge code faster and with higher quality. This tool is designed to assist with various aspects of PR review, from summarizing changes to identifying potential issues.

## Features

This project offers (or aims to offer) the following features:

*   **PR Summarization:** Generates concise summaries of the changes introduced in a pull request, making it easier to understand the purpose and scope of the PR at a glance.
*   **Code Quality Assessment:** Analyzes the code for potential bugs, style violations, complexity, and adherence to best practices.
*   **Security Vulnerability Detection:** Scans the codebase for potential security vulnerabilities using a combination of static analysis and LLM-powered understanding.
*   **Test Suggestions:** Intelligently suggests relevant tests that should be added or modified based on the code changes.
*   **Effort and Risk Estimation:** Provides a rough estimation of the effort required to review the pull request and the potential risk associated with merging it.
*   **Related Issue/PR Linking:** Automatically identifies and links related GitHub issues and other pull requests, providing more context for reviewers.
*   **Sentiment Analysis:** Detects the overall sentiment of the PR description and comments, helping to gauge the tone of the discussion.

## Getting Started

### Prerequisites

*   Python 3.12+
*   A GitHub account and a personal access token (with `repo` scope) - [Create one here](https://github.com/settings/tokens/new)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Skalyne/PR_AI_Analysis.git
    cd PR_AI_Analysis
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. Create a `.env` file in the project root and add your GitHub personal access token:
   ```
   GITHUB_TOKEN=your_github_token
   GOOGLE_AI_TOKEN=yourgemii_token
   ```

2. Run the main script:
    update pr_url variable with this format: https://api.github.com/repos/{Owner}/{Repository}/pulls/{PR_number}

## Roadmap

Future development plans include:

*   **Improved LLM Fine-tuning:** Fine-tune the LLMs on a large dataset of code reviews to improve accuracy and relevance.
*   **Integration with GitHub Actions:**  Create a GitHub Action to automatically analyze pull requests as part of a CI/CD pipeline.
*   **Customizable Configuration:** Allow users to configure the analysis rules and thresholds to their specific needs.
*   **Support for other version control systems:** Extend support beyond GitHub to platforms like GitLab and Bitbucket.
*   **Web Interface:** Develop a user-friendly web interface for interacting with the tool.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them with clear and concise commit messages.
4. Push your branch to your forked repository: `git push origin feature/your-feature-name`
5. Open a pull request against the `main` branch of this repository.

Please ensure your code adheres to the project's coding style and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

*   [Gemini](https://ai.google.dev/gemini-api/docs?hl=es-419)
*   [GitHub API](https://docs.github.com/en/rest)

## Disclaimer

This tool is still under development and may produce inaccurate or incomplete results. Use it as a supplementary aid for code review, not as a replacement for human judgment.