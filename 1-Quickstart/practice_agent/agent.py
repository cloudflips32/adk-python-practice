from google.adk.agents.llm_agent import Agent
from datetime import datetime

def get_current_time(city: str) -> dict:
    """Get the current time in a given city"""
    return { "status": "success", "data": { "time": datetime.now().strftime("%H:%M:%S")}}

root_agent = Agent (
    model='gemini-2.5-flash',
    name='root_agent',
    description="Tell the current time in a given city. Its free!",
    instruction="You are a helpful assistant that tells the current time in a given city. Its free after all! Use the 'get_current_time' tool in order to do this.",
    tools=[get_current_time],
)

