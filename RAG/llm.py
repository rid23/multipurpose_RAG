import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

class AIClient:
    def __init__(self):
        self.url = "https://generativelanguage.googleapis.com/v1beta/openai/v1/chat/completions"
        self.headers = {
            "Authorization":f"Bearer {API_KEY}",
            "Content-Type":"application/json"
        }

    def ask(self,prompt):

        data = {
            "model":"gemini-2.5-flash",
            "messages":[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        }

        for _ in range(3):
            try:
                response = requests.post(url=self.url,
                                         headers=self.headers,
                                         json=data,
                                         timeout=10)
                if response.status_code != 200:
                    return response.text

                reply = response.json()["choices"][0]["message"]["content"]

                return reply
            except Exception as e:
                print("ERROR: ",e)
                print("Retrying...")
