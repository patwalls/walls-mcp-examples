"""
Use Superhighway's paid web tools inside a LlamaIndex agent.

The MCP server is loaded over stdio; your agent gets web_search, news_search,
scrape, geocode, nlp, email_verify, convert, and qr — each paid per call in USDC
on Base via x402, with a wallet you control. No API key, no signup.

    pip install llama-index llama-index-tools-mcp llama-index-llms-openai
    export AGENT_PRIVATE_KEY=0xYOUR_FUNDED_BASE_WALLET_KEY
    export OPENAI_API_KEY=...        # or swap in any LlamaIndex LLM
    python examples/llamaindex_agent.py
"""
import asyncio
import os

from llama_index.tools.mcp import BasicMCPClient, McpToolSpec
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI


async def main() -> None:
    client = BasicMCPClient(
        "npx",
        args=["-y", "github:patwalls/superhighway-mcp"],
        env={
            "AGENT_PRIVATE_KEY": os.environ["AGENT_PRIVATE_KEY"],
            "X402_NETWORK": "base",
        },
    )

    tools = await McpToolSpec(client=client).to_tool_list_async()
    print("Loaded tools:", [t.metadata.name for t in tools])

    agent = FunctionAgent(tools=tools, llm=OpenAI(model="gpt-4o-mini"))
    response = await agent.run("Search the web for the latest on the x402 protocol and summarize the top result.")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
