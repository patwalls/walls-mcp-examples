"""
Use Superhighway's paid web tools inside a LangChain / LangGraph agent.

The MCP server is loaded over stdio; your agent gets web_search, news_search,
scrape, geocode, nlp, email_verify, and convert — each paid per call in USDC on
Base via x402, with a wallet you control. No API key, no signup.

    pip install langchain-mcp-adapters langgraph langchain-openai
    export AGENT_PRIVATE_KEY=0xYOUR_FUNDED_BASE_WALLET_KEY
    export OPENAI_API_KEY=...        # or swap in any LangChain chat model
    python examples/langchain_agent.py
"""
import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent


async def main() -> None:
    client = MultiServerMCPClient(
        {
            "superhighway": {
                "command": "npx",
                "args": ["-y", "superhighway-mcp"],
                "transport": "stdio",
                "env": {
                    "AGENT_PRIVATE_KEY": os.environ["AGENT_PRIVATE_KEY"],
                    "X402_NETWORK": "base",
                },
            }
        }
    )

    tools = await client.get_tools()
    print("Loaded tools:", [t.name for t in tools])

    agent = create_react_agent(ChatOpenAI(model="gpt-4o-mini"), tools)
    result = await agent.ainvoke(
        {"messages": "Search the web for the latest on the x402 protocol and summarize the top result."}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
