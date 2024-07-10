from agents.agent import Agent
from models.Ollama_models import OllamaModel
from models.Openai_models import Openai_model
from tools.reverse import reverse_string
if __name__ == "__main__":
    tools = [reverse_string]
    agent_instance= Agent(model_service=Openai_model,model_name='gpt-3.5-turbo',tools=tools)
    while True:
        prompt = input("Input your prompt: ")
        if prompt.lower() =="exit":
            break
        agent_instance.work(prompt=prompt)