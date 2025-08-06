from fastmcp import FastMCP
from dotenv import load_dotenv
from colorama import Fore
import asyncio
from sympy import *
mcp = FastMCP("MCPTools")
@mcp.tool()
def check_prime(number: int = 0):
    """
    check if the number is a prime

    Args:
        number (int, optional): the number given. Defaults to 0.
    """
    is_prime_flag = isprime(number)
    if is_prime_flag:
        out="it is a prime number"
    else:
        out="it is not a prime number"

    return out

mcp.run(transport="streamable-http",
        host="127.0.0.1",
        port=4200,
        log_level="debug",
        )
