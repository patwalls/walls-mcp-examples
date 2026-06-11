# walls-mcp-examples

**Give your AI agent web search in one line — no API key, no signup.**

Working examples for adding [Superhighway](https://superhighway.walls.sh) — web search for
AI agents — to any MCP agent (Claude Desktop, Cursor, Windsurf, …). Your agent searches the
live web, pulls recent news, and reads any page as clean markdown; under the hood it pays
**per call in USDC on Base via [x402](https://x402.org)** with a wallet you control.

Superhighway is **Wall #001** of [walls.sh](https://walls.sh) — a directory of businesses that
AI agents pay for.

## The tools

| Tool | What it does | Price |
|---|---|---|
| `web_search` | Live web search → ranked results as clean JSON | $0.001 |
| `news_search` | Recent news articles with published dates | $0.001 |
| `image_search` | Image search → image URLs, source pages, thumbnails | $0.001 |
| `scrape` | Read any page → title + clean markdown + text | $0.002 |
| `research` | Search + read the top pages in one call | $0.005 |

## Try it free first (no wallet)

Open **[superhighway.walls.sh](https://superhighway.walls.sh)** and run a search in the box —
no wallet, no signup. When you're ready to give it to your agent, set up the MCP server below.

## 5-minute setup

New to this? Follow **[TUTORIAL.md](TUTORIAL.md)** — wallet → fund → config → ask, step by step.

## Install (Claude Desktop / Cursor / Windsurf)

Add this to your MCP client config (`claude_desktop_config.json`, Cursor `mcp.json`, etc.):

```json
{
  "mcpServers": {
    "superhighway": {
      "command": "npx",
      "args": ["-y", "superhighway-mcp"],
      "env": {
        "AGENT_PRIVATE_KEY": "0xYOUR_FUNDED_BASE_WALLET_KEY",
        "X402_NETWORK": "base"
      }
    }
  }
}
```

Restart your client. Your agent now has the whole search job in five tools: `web_search`, `news_search`, `image_search`, `scrape`, and `research` (search + read in one call). Find it, read it, pay per call.
See [`examples/claude_desktop_config.json`](examples/claude_desktop_config.json).

## Get a wallet

`AGENT_PRIVATE_KEY` is any EVM wallet you control, funded with a little **USDC on Base** (each
call is $0.001–$0.002; gas is covered by the facilitator, so you don't need ETH). Keep a small
balance — the key only ever signs tiny USDC payments. Generate one with viem:

```bash
node -e 'const {generatePrivateKey}=require("viem/accounts");console.log(generatePrivateKey())'
```

Want to pay in **test** USDC first? Set `X402_NETWORK=base-sepolia` and fund the address from a
[Base Sepolia faucet](https://faucet.circle.com).

## Use it in an agent framework

- **LangChain / LangGraph** → [`examples/langchain_agent.py`](examples/langchain_agent.py)
- **LlamaIndex** → [`examples/llamaindex_agent.py`](examples/llamaindex_agent.py)
- **CrewAI** → [`examples/crewai_agent.py`](examples/crewai_agent.py)

<details><summary>LangChain quickstart</summary>

Load the tools into a LangChain/LangGraph agent — see [`examples/langchain_agent.py`](examples/langchain_agent.py):

```bash
pip install langchain-mcp-adapters langgraph langchain-openai
AGENT_PRIVATE_KEY=0x... python examples/langchain_agent.py
```
</details>

## Use it in n8n

Install the native community node — no HTTP wiring needed:

1. **Settings → Community Nodes → Install**, enter `n8n-nodes-superhighway`
2. Add a **Superhighway** node to your workflow, create a **Superhighway API** credential with a free API key from [/pricing](https://superhighway.walls.sh/pricing)
3. Choose an operation (Web Search, News Search, Image Search, Read Page, Research), enter a query, execute

Full guide: [Add live web search to n8n, Make, or Zapier workflows](https://superhighway.walls.sh/guides/web-search-n8n-make-zapier)

## Use it without MCP (raw x402)

Any agent that can sign an x402 payment can call the API directly — see
[`examples/agent.mjs`](examples/agent.mjs):

```bash
npm i x402-fetch viem
AGENT_PRIVATE_KEY=0x... X402_NETWORK=base node examples/agent.mjs "best espresso machines"
```

## How it compares

See **[COMPARISON.md](COMPARISON.md)** — Superhighway vs. ScrapingBee / Serper / ScreenshotOne / Google Geocoding (pay-per-call, no API key, no signup).

## Guides

Step-by-step documentation on superhighway.walls.sh:

- [Add live web search to Claude Code (or any MCP client)](https://superhighway.walls.sh/guides/add-web-search-to-claude-code) — install the MCP server, fund a wallet, use the five tools
- [Add live web search to a LangChain, LlamaIndex, or CrewAI agent](https://superhighway.walls.sh/guides/web-search-langchain-llamaindex-crewai) — MCP adapter + REST API paths for Python frameworks
- [Add live web search to an OpenAI Agents SDK agent](https://superhighway.walls.sh/guides/web-search-openai-agents-sdk) — MCPServerStdio path or @function_tool with an API key
- [A web search API your AI agent can pay for by itself](https://superhighway.walls.sh/guides/web-search-api-agents-pay-per-call) — the x402 pay-per-call flow, step by step
- [Image search for AI agents: direct URLs, thumbnails, and visual context](https://superhighway.walls.sh/guides/image-search-for-ai-agents) — use `/images` for visual grounding and multimodal agents
- [Get answers, not links: search + read the top pages in one API call](https://superhighway.walls.sh/guides/search-and-read-in-one-call) — the `/research` endpoint explained
- [Add live web search to n8n, Make, or Zapier workflows](https://superhighway.walls.sh/guides/web-search-n8n-make-zapier) — native n8n community node + HTTP Request for Make/Zapier

## Links

- Package: https://github.com/patwalls/superhighway-mcp
- Live API + free demo: https://superhighway.walls.sh
- Guides: https://superhighway.walls.sh/guides
- The directory: https://walls.sh
- x402 protocol: https://x402.org

MIT.
