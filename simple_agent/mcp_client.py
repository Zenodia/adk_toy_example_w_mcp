import asyncio

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
from fastmcp.tools import Tool
from colorama import Fore

async def main():
    client = Client(transport=StreamableHttpTransport("http://127.0.0.1:4200/mcp"))
    async with client:
        tools: list[Tool] = await client.list_tools()
        for tool in tools:
            print(f"Tool: {tool}")

        result = await client.call_tool("check_prime", {"number": 3})
        print(Fore.YELLOW + f"type(result) , {type(result.content)} | result: {result.content[0].text}", Fore.RESET)
    

if __name__ == "__main__":
    asyncio.run(main())