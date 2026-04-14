from google.adk.agents.llm_agent import Agent

def get_powershell_commands(command: str) -> dict:
    """ Get necessary powershell commands for a given task """
    return { "status": "success", "report": f"The powershell command that you are looking for is {command}" }

def get_bash_commands(command: str) -> dict:
    """ Get necessary bash commands for a given task """
    return { "status": "success", "report": f"The bash command that you are looking for is {command}" }

def get_cmd_commands(command: str) -> dict:
    """ Get necessary command prompt commands for a given task """
    return { "status": "success", "report": f"The command prompt command that you are looking for is {command}" }


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful terminal command learning assistant for user questions.',
    instruction='Help the user better learn how to use Windows Powershell, the Linux Bash terminal, and the Windows Command Prompt by digesting user queries and providing the correct command for their needs. Be sure to verify the correct terminal, as well as the correct command for the given task.',
    tools=[get_powershell_commands, get_bash_commands, get_cmd_commands],
)
