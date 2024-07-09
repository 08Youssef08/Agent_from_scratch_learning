import os
import requests
import json
class Openai_model:
    def __init__(self,temperature,model_name,system_prompt,model_endpoint):
        self.model_name=model_name
        self.temperature=temperature,
        self.system_prompt=system_prompt
        self.model_endpoint=model_endpoint
        self.api_key= os.getenv('OPENAI_API_KEY')
        self.header={"Content-Type": "application/json"
                     ,"Authorization": f"Bearer ${self.api_key}"}
    def generate_text(self,prompt):
        payload= {
    "model": self.model_name,
    "response_format": { "type": "json_object" },
    "messages": [
      {
        "role": "system",
        "content": self.system_prompt,
      },
      {
        "role": "user",
        "content": prompt
      }
    ],
    "stream": False,
    "temperature": self.temperature,
  }
        response_dict= requests.post(self.model_endpoint,headers=self.header,data=json.dump(payload))
        response_json= response_dict.json()
        response= json.load(response_json['choices'][0]['message']['content'])
        print(F"\n\nResponse from OpenAI model: {response}")
        return response


