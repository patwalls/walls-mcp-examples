# Give your Claude (or Cursor) agent web tools in 5 minutes

Your agent can't search the web, read a page, geocode an address, or check an email —
unless you wire up tools. This adds **six** of them in one line, and your agent **pays
per call in USDC** (via [x402](https://x402.org)) with a wallet you control. No API key,
no signup, no subscription.

The tools: `web_search`, `news_search`, `scrape` (read any page as markdown), `geocode`
(address ↔ coordinates), `nlp` (language/sentiment/keywords/summary), `email_verify`.

## 0. Try it free first (30 seconds, no wallet)

Open **[superhighway.walls.sh](https://superhighway.walls.sh)** and run a search in the box.
That's the same engine your agent will call — just paid, per call, when an agent uses it.

## 1. Make a wallet

Any EVM wallet works. Generate one:

```bash
node -e 'const {generatePrivateKey}=require("viem/accounts");console.log(generatePrivateKey())'
```

Save the `0x…` private key. (Or use the `X402_NETWORK=base-sepolia` testnet first — see step 5.)

## 2. Fund it with a little USDC on Base

Send **$1–$5 of USDC on the Base network** to that wallet's address. Each call costs
$0.001–$0.002, and **gas is covered by the facilitator** — so you don't need ETH, just USDC.

> From Coinbase: Convert a little to USDC → Send → paste the address → **choose the Base
> network** → send. (Base, not Ethereum — Base keeps fees near zero.)

## 3. Add the MCP server to your client

**Claude Desktop** (`claude_desktop_config.json`) / **Cursor** (`mcp.json`) / **Windsurf**:

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

## 4. Restart your client, then ask

Your agent now has the six tools. Try prompts like:

- "**Search** the web for the latest on x402 and summarize the top 3 results."
- "**Scrape** https://x402.org and give me the key points."
- "What are the **coordinates** of the Sydney Opera House?" (geocode)
- "Run **sentiment** analysis on this review: …" (nlp)
- "Is `founder@acme.com` a **deliverable** email?" (email_verify)

The agent calls the tool, pays $0.001–$0.002 from your wallet, and gets the result — no
key, no human in the loop.

## 5. Test for free on testnet (optional)

Set `X402_NETWORK=base-sepolia` and fund the wallet with test USDC from the
[Base Sepolia faucet](https://faucet.circle.com). Everything works identically, in play money.

## Troubleshooting

- **Tools don't appear** → fully quit and reopen the client; confirm the JSON is valid.
- **Payments fail** → make sure the wallet has **USDC on Base** (not Ethereum) and `X402_NETWORK=base`.
- **First run is slow** → `npx` installs the server the first time; subsequent runs are instant.
- **Want to keep a low balance** → the key only ever signs tiny USDC payments; keep just a few dollars.

## Use it without MCP

Any agent that can sign an x402 payment can call the API directly — see
[`examples/agent.mjs`](examples/agent.mjs).

---

Built on [Superhighway](https://superhighway.walls.sh) — Wall #001 of [walls.sh](https://walls.sh),
a directory of businesses AI agents pay for. See [COMPARISON.md](COMPARISON.md) for how it stacks up
against ScrapingBee / Serper / ScreenshotOne / Google Geocoding.
