# walls-mcp-examples

**Give your AI agent paid web tools in one line — no API key, no signup.**

Working examples for adding [Superhighway](https://superhighway.walls.sh)'s tools to any
MCP agent (Claude Desktop, Cursor, Windsurf, …). Your agent calls a tool; under the hood it
pays **per call in USDC on Base via [x402](https://x402.org)** with a wallet you control.

Superhighway is **Wall #001** of [walls.sh](https://walls.sh) — a directory of businesses that
AI agents pay for.

## The tools

| Tool | What it does | Price |
|---|---|---|
| `web_search` | Real-time web search → ranked results | $0.001 |
| `news_search` | Recent news articles | $0.001 |
| `scrape` | Read any page as clean markdown | $0.002 |
| `geocode` | Address ↔ coordinates (forward/reverse) | $0.001 |

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
      "args": ["-y", "github:patwalls/superhighway-mcp"],
      "env": {
        "AGENT_PRIVATE_KEY": "0xYOUR_FUNDED_BASE_WALLET_KEY",
        "X402_NETWORK": "base"
      }
    }
  }
}
```

Restart your client. Your agent now has `web_search`, `news_search`, `scrape`, and `geocode`.
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

<details><summary>LangChain quickstart</summary>

Load the tools into a LangChain/LangGraph agent — see [`examples/langchain_agent.py`](examples/langchain_agent.py):

```bash
pip install langchain-mcp-adapters langgraph langchain-openai
AGENT_PRIVATE_KEY=0x... python examples/langchain_agent.py
```
</details>

## Use it without MCP (raw x402)

Any agent that can sign an x402 payment can call the API directly — see
[`examples/agent.mjs`](examples/agent.mjs):

```bash
npm i x402-fetch viem
AGENT_PRIVATE_KEY=0x... X402_NETWORK=base node examples/agent.mjs "best espresso machines"
```

## How it compares

See **[COMPARISON.md](COMPARISON.md)** — Superhighway vs. ScrapingBee / Serper / ScreenshotOne / Google Geocoding (pay-per-call, no API key, no signup).

## Links

- Package: https://github.com/patwalls/superhighway-mcp
- Live API + free demo: https://superhighway.walls.sh
- The directory: https://walls.sh
- x402 protocol: https://x402.org

MIT.
