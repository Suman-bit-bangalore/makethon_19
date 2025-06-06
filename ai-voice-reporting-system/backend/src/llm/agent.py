from typing import Any, Dict, List
import requests

class LLMAgent:
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
        self.conversation_history = []

    def add_to_history(self, user_input: str, bot_response: str):
        self.conversation_history.append({"user": user_input, "bot": bot_response})

    def clear_history(self):
        self.conversation_history = []

    def generate_prompt(self, user_input: str) -> str:
        context = "\n".join([f"User: {entry['user']}\nBot: {entry['bot']}" for entry in self.conversation_history])
        return f"{context}\nUser: {user_input}\nBot:"

    def query_llm(self, user_input: str) -> str:
        prompt = self.generate_prompt(user_input)
        response = requests.post(
            "https://api.example.com/v1/engines/{}/completions".format(self.model),
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"prompt": prompt, "max_tokens": 150}
        )
        response_data = response.json()
        return response_data.get("choices", [{}])[0].get("text", "").strip()

    def respond_to_user(self, user_input: str) -> str:
        bot_response = self.query_llm(user_input)
        self.add_to_history(user_input, bot_response)
        return bot_response
