import re, json
import google.generativeai as genai
from environment_variables import GOOGLE_AI_TOKEN

class DiffAnalysis:
    """
    Analyzes a code diff using Google's generative AI (Gemini) to provide feedback and suggest improvements.

    The class takes a code diff as input, constructs a prompt for the Gemini model,
    and then parses the model's response to extract a list of comments in a specific format.

    Attributes:
        diff (str): The code diff to be analyzed.
        model (genai.GenerativeModel): The initialized Gemini model.
        prompt (str): The prompt sent to the Gemini model for code review.
    """
    def __init__(self, diff):
        """
        Initializes the DiffAnalysis object with the given code diff and sets up the Gemini model.

        Args:
            diff (str): The code diff to be analyzed.
        """
        self.diff = diff
        self.model = self._setup_gemini_model()
        self.prompt = self._create_prompt()

    def _setup_gemini_model(self):
        """
        Configures and initializes the Gemini model.

        Returns:
            genai.GenerativeModel: The initialized Gemini model.
        """
        genai.configure(api_key=GOOGLE_AI_TOKEN)
        return genai.GenerativeModel("gemini-1.5-flash")

    def _create_prompt(self):
        """
        Constructs the prompt to be sent to the Gemini model for code review.

        Returns:
            str: The formatted prompt.
        """
        inline_comment_format = """
            {
                "body": (str) The body text of the pull request review.
                "comments": (list[dict])[
                    "path": (str) The relative path to the file that necessitates a review comment.
                    "line": (int) line for comment
                    "body": (str) Text of the review comment.
                ]
            }
        """
        prompt = f"""You are a highly skilled Python code reviewer. Analyze the following code diff from a pull request and provide feedback.

            Focus on:
            - Identifying potential bugs or logic errors.
            - Suggesting improvements for code efficiency and clarity.
            - Providing specific line-level recommendations when possible.
            - Offering general feedback on the overall code quality.
            - Just on python files
            - avoid regular expresions or regex

            you MUST return a python list that contain a dict element, the dict element MUST match with this exact format:
            ```
            {inline_comment_format}
            ```
            remember that `comments` key is a list where you have to add a element for each comment you want to address
            
            Code Diff:
            ```
            {self.diff}
            ```
        """
        return prompt

    def _extract_python_list_from_response(self, response_text):
        """
        Extracts and parses a JSON object from the Gemini model's response.

        It searches for the JSON object within triple backticks (```) and handles
        cases where the response might be surrounded by triple quotes and backticks.

        Args:
            response_text (str): The raw response text from the Gemini model.

        Returns:
            dict or None: The parsed JSON object if found, otherwise None.
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
        """
        Generates the code review response from the Gemini model and extracts the JSON object.

        Returns:
            dict or str: The parsed JSON object containing the review comments if successful,
            otherwise an error message.
        """
        response = self.model.generate_content(self.prompt)
        extracted_list = self._extract_python_list_from_response(response.text)
        if extracted_list:
            return extracted_list
        else:
            return "No Python list found in the response."
