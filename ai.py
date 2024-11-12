import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API"))


class gemini_ai():
    def __init__(self):
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=self.generation_config,)
        self.chat = self.model.start_chat(history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ])

    def get_answer(self, question):
        response = self.chat.send_message(question, stream=True)
        ans = ''
        for chunk in response:
            ans += chunk.text
        return ans

    def get_history(self):
        return (self.chat.history)

    def clear_history(self):
        self.chat = self.model.start_chat(history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ])
