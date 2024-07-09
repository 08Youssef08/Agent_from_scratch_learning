from toolbox.toolbox import Toolbox
from prompts.prompts import agent_system_prompt_template
from models.Ollama_models import OllamaModel
class Agent:
    def __init__(self,model_name,tools,model_service,stop=None):
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
                
            )


