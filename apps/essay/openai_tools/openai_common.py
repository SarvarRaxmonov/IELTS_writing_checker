import openai

OPENAI_API_KEY = "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"


system_role_in_ielts = """
        You know everything about scoring IELTS essays. You assess the given essay of the given question and provide
        feedback to help the writer to improve in the future, and specify mistakes and suggest corrections.
        """
default_system_role = """
        You're in capable hands. You have extensive knowledge on this topic. 
        Please proceed with provided questions or requests, and we'll provide you with the information you need.
"""

model = "gpt-3.5-turbo-0613"


openai.api_key = OPENAI_API_KEY

open_ai = openai
