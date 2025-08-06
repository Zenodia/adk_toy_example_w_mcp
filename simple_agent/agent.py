from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

import getpass
import os
import random
from sympy import *
import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
from fastmcp.tools import Tool
from colorama import Fore

if os.environ.get("NVIDIA_API_KEY", "").startswith("nvapi-"):
    print("Valid NVIDIA_API_KEY already in environment. Delete to reset")
else:
    nvapi_key = getpass.getpass("NVAPI Key (starts with nvapi-): ")
    assert nvapi_key.startswith("nvapi-"), f"{nvapi_key[:5]}... is not a valid key"
    os.environ["NVIDIA_API_KEY"] = nvapi_key
def roll_die():
    """
    Roll a die

    Args:
        
    """    
    dice_nr=[1,2,3,4,5,6]
    nr=random.sample(dice_nr,1)
    return {"status":"success","report": nr[0]}

"""
def check_prime(number: int = 0):
    
    is_prime_flag = isprime(number)
    if is_prime_flag:
        out="it is a prime number"
    else:
        out="it is not a prime number"

    return {"status": "success", "report": out}
"""
async def check_prime():
    """
    check if the number is a prime
    Args:
        number (int, optional): the number given. Defaults to 0.
    """
    client = Client(transport=StreamableHttpTransport("http://127.0.0.1:4200/mcp"))
    async with client:
        tools: list[Tool] = await client.list_tools()
        for tool in tools:
            print(f"Tool: {tool}")

        result = await client.call_tool("check_prime", {"number": 3})
        #print(Fore.YELLOW + f"type(result) , {type(result.content)} | result: {result.content[0].text}", Fore.RESET)
        out=result.content[0].text
    return out

base_url = "https://integrate.api.nvidia.com/v1"
root_agent = Agent(
    model=LiteLlm(model="openai/meta/llama-3.1-405b-instruct", base_url=base_url, api_key=os.environ["NVIDIA_API_KEY"]),
    name="dice_agent",
    description=(
        "hello world agent that can roll a dice of 6 sides and check prime"
        " numbers."
    ),
    instruction="""
      You roll dice and answer questions about the outcome of the dice rolls.
    """,
    tools=[
        roll_die,
        check_prime,
    ],
)