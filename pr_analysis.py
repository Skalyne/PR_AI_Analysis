import re, json
import google.generativeai as genai
from environment_variables import GOOGLE_AI_TOKEN

class DiffAnalysis:
    def __init__(self, diff):
        self.diff = diff
        inline_comment_format = '''
            {
                "body": (str) The body text of the pull request review.
                "comments": (list[dict])[
                    "path": (str) The relative path to the file that necessitates a review comment.
                    "line": (int)
                    "body": (str) Text of the review comment.
                ]
            }
        '''

        self.promt = f"""You are a highly skilled Python code reviewer. Analyze the following code diff from a pull request and provide feedback.

            Focus on:
            - Identifying potential bugs or logic errors.
            - Suggesting improvements for code efficiency and clarity.
            - Providing specific line-level recommendations when possible.
            - Offering general feedback on the overall code quality.
            - Just on python files

            you MUST return a python list that contain a dict element, the dict element MUST match with this exact format:
            ```
            {inline_comment_format}
            ```
            remember that `comments` key is a list where you have to add a element for each comment you want to address
            
            Code Diff:
            ```
            {diff}
            ```
        """
        genai.configure(api_key=GOOGLE_AI_TOKEN)
        self.model = genai.GenerativeModel("gemini-1.5-flash")


    def _extract_python_list_from_response(self, response_text):
        """
        Extracts a Python list from a string that contains the list enclosed in triple backticks.

        Args:
            response_text: The string containing the response, including the triple backticks.

        Returns:
            The extracted Python list as a string, or None if no list is found.
        """
        match = re.search(r"```python\n(.*?)```", response_text, re.DOTALL)
        if match:
            return json.loads(match.group(1).strip())
        else:
            match = re.search(r'"""([\s\S]*?)```python\n(.*?)\n```([\s\S]*?)"""', response_text, re.DOTALL)
            if match:
                extracted_list_str = match.group(2)
                return json.loads(extracted_list_str)
            else:
                return None

    def generate_response(self):
        response = self.model.generate_content(self.promt)
        extracted_list = self._extract_python_list_from_response(response.text)
        if extracted_list:
            return extracted_list
        else:
            return "No Python list found in the response."
