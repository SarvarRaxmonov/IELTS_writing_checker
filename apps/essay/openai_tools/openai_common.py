import openai

OPENAI_API_KEY = "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"


system_role_in_ielts = """
        You know everything about scoring IELTS essays. You assess the given essay of the given question and provide
        feedback to help the writer to improve in the future, and specify mistakes and suggest corrections.
        """

model = "gpt-3.5-turbo-0613"


openai.api_key = OPENAI_API_KEY

open_ai = openai

