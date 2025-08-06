from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

import getpass
import os
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
    # ... function logic ...
    return {"status":"success","report": 2}

def check_prime(number: int = 0):
    """
    check if the number is a prime

    Args:
        number (int, optional): the number given. Defaults to 0.
    """
    
    return {"status": "success", "report": f"it is a prime number"}
base_url = "https://integrate.api.nvidia.com/v1"
root_agent = Agent(
    model=LiteLlm(model="openai/meta/llama-3.1-405b-instruct", base_url=base_url, api_key=os.environ["NVIDIA_API_KEY"]),
    name="dice_agent",
    description=(
        "hello world agent that can roll a dice of 8 sides and check prime"
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