from toolbox.toolbox import Toolbox
from prompts.prompts import agent_system_prompt_template
from models.Ollama_models import OllamaModel
from models.Openai_models import Openai_model
from termcolor import colored

class Agent:
    def __init__(self,model_service,model_name,tools,stop=None):
        '''
        Initialise the parameters from tools and a model for the agent
        Parameters:
            model_name(str): name of the model
            model_service(class): service type whether it's Local or openai
            tools(list): list of tools that the agent could use
        '''
        self.model_name=model_name
        self.model_service=model_service
        self.tools=tools
        self.stop=stop
    def prepare_tools(self):
        '''
        prepares the string of tool names and their docstrings
        Returns:
            str: tools dictionary as a string
        '''
        tool=Toolbox()
        tool.store(self.tools)
        tool_description= tool.tools()
        return tool_description
    def think(self,prompt):
        '''
        generates the text from the model using the tools and the prompt before passing it to generate the json file 

        Parameters:

        '''
        description_tools= self.prepare_tools()
        agent_system_prompt= agent_system_prompt_template.format(description_tools)
        if self.model_service == OllamaModel:
            model_instance=self.model_service(
                model=self.model_name,
                system_prompt=agent_system_prompt,
                temperature=0,
                stop=self.stop)
        else:
            model_instance= Openai_model(
                model=self.model_name,
                system_prompt=agent_system_prompt,
                temperature=0                
            ) 
        response_dict = model_instance.generate_text(prompt=prompt)
        return response_dict
    def work(self,prompt):
        response_dict= self.think(prompt)
        tool_choice=response_dict.get("tool_choice")
        tool_input=response_dict.get("tool_input")
        response=""
        for tool in self.tools:
            if tool.__name__== tool_choice:
                response=tool(tool_input)
                print(colored(response, 'cyan'))
                return
                # leave with a tool reply

        print(colored(tool_input, 'cyan'))
        
        return
        #leave with a direct query with no-tool
            

    
            


