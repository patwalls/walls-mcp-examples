"""
Use Superhighway's paid web tools inside a CrewAI crew.

The MCP server is loaded over stdio via CrewAI's MCPServerAdapter; your agents get
web_search, news_search, scrape, geocode, nlp, email_verify, convert, qr, feed, and
sitemap — each paid per call in USDC on Base via x402, with a wallet you control.
No API key, no signup.

    pip install 'crewai-tools[mcp]' crewai
    export AGENT_PRIVATE_KEY=0xYOUR_FUNDED_BASE_WALLET_KEY
    export OPENAI_API_KEY=...        # or configure any LLM CrewAI supports
    python examples/crewai_agent.py
"""
import os

from crewai import Agent, Crew, Task
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters

# Boot the Superhighway MCP server over stdio. It pays per call with YOUR wallet.
server_params = StdioServerParameters(
    command="npx",
    args=["-y", "superhighway-mcp"],
    env={
        "AGENT_PRIVATE_KEY": os.environ["AGENT_PRIVATE_KEY"],
        "X402_NETWORK": "base",
        # Inherit PATH so `npx` resolves.
        "PATH": os.environ.get("PATH", ""),
    },
)

# MCPServerAdapter exposes the server's tools as CrewAI tools for the duration
# of the `with` block (the subprocess is cleaned up on exit).
with MCPServerAdapter(server_params) as superhighway_tools:
    print("Loaded tools:", [t.name for t in superhighway_tools])

    researcher = Agent(
        role="Web Researcher",
        goal="Answer questions using live web tools, paying per call in USDC.",
        backstory=(
            "A self-funding research agent. It carries its own Base wallet and "
            "buys exactly the web calls it needs — no API keys, no subscriptions."
        ),
        tools=superhighway_tools,
        verbose=True,
    )

    task = Task(
        description=(
            "Search the web for the latest on the x402 protocol, then read the "
            "single most relevant result and summarize it in 3 bullet points."
        ),
        expected_output="Three concise bullet points summarizing the top source.",
        agent=researcher,
    )

    crew = Crew(agents=[researcher], tasks=[task], verbose=True)
    print(crew.kickoff())
