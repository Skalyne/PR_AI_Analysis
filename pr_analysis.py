import google.generativeai as genai
from environmet_variables import GEMINI_TOKEN

class DiffAnalysis:
    def __init__(self, diff):
        self.diff = diff
        self.promt = f"""You are a highly skilled Python code reviewer. Analyze the following code diff from a pull request and provide feedback.

            Focus on:
            - Identifying potential bugs or logic errors.
            - Suggesting improvements for code efficiency and clarity.
            - Providing specific line-level recommendations when possible.
            - Offering general feedback on the overall code quality.

            Code Diff:
            ```
            {diff}
            ```
            you MUST return a list that contain a json element for each file
            json MUST match with this fotmat exact format:
            
            `body`:`the review`
            `path`:`File that is afected`
            `start_line`:int
            `line`:int
            
        """
        genai.configure(api_key=GEMINI_TOKEN)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_response(self):
        return self.model.generate_content(self.promt)
    
    