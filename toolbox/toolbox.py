class Toolbox:
    def __init__(self):
        self.tools_dict= {}
    def store(self,tools_list):
        '''
        Stores the name of the tools alongside their description in a dict

        Parameters:
            tools(list): A list of all the tools
        Returns:
            Dict(dict): a dict with function names as key and their docstring as value
        '''
        for func in tools_list:
            self.tools_dict[func.__name__]=func.__doc__
        return self.tools_dict

    def tools(self):
        '''
        Turns the tool dictionary into a string of tools

        Returns:
            str: string of the tool dictionary
        '''
        tool_str=""
        for name,desc in self.tools_dict.items():
            tool_str+= f"{name}: \"{desc}\" \n"
        return tool_str
