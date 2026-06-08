# Web tools for AI agents: Superhighway vs. the alternatives

If you're giving an AI agent web access — search, scraping, geocoding, text analysis —
you've probably looked at ScrapingBee, ScreenshotOne, Brave Search API, Serper, Google
Geocoding, and friends. They're good APIs. But they were all built for a **human** to
sign up, get an API key, and put a card on file.

[Superhighway](https://superhighway.walls.sh) is built for the **agent**: it pays per
call in USDC over HTTP (the [x402](https://x402.org) protocol). No signup, no API key,
no subscription, no dashboard. One `npx` line and your agent has tools it pays for itself.

## The difference that matters for agents

| | Superhighway | Typical API (ScrapingBee / Serper / ScreenshotOne / Google Geocoding) |
|---|---|---|
| **Signup / account** | None | Required |
| **API key** | None | Required (a human creates + rotates it) |
| **Pricing model** | Pay **per call** in USDC | Monthly plans / credit packs / committed tiers |
| **Minimum commitment** | $0 — pay for exactly what you use | Usually a plan or minimum |
| **Who can buy** | An **agent** with a wallet, autonomously | A human, via a signup funnel an agent can't navigate |
| **Settlement** | On-chain, ~12s, no chargebacks | Card on file / invoice |
| **Setup for an agent** | One MCP line (`npx -y github:patwalls/superhighway-mcp`) | Provision key → store secret → wire SDK |

Superhighway isn't trying to out-feature mature single-purpose APIs. The wedge is the
**purchase model**: an agent can discover, pay for, and use it in one autonomous round-trip,
which a key-and-card API fundamentally can't offer.

## What you get (one install, five tools)

| Tool | Replaces (roughly) | Price/call |
|---|---|---|
| `web_search` | Brave Search API / Serper / SerpAPI | $0.001 |
| `news_search` | News API tiers | $0.001 |
| `scrape` | ScrapingBee / ScrapingAnt (read a page → markdown) | $0.002 |
| `geocode` | Google Geocoding / geocode.xyz (address ↔ coords) | $0.001 |
| `nlp` | A small NLP API or an LLM round-trip (language/sentiment/keywords/summary) | $0.001 |

## When to use which

- **Use Superhighway** when an autonomous agent needs web tools *and you don't want to
  provision/rotate API keys or commit to a plan* — especially for many small agents, each
  paying for exactly what it uses.
- **Use a dedicated incumbent** when you need that one capability at high scale with SLAs,
  enterprise support, or features beyond the basics. (You can use both.)

## Try it (free, no wallet)

Run a search in the box at **[superhighway.walls.sh](https://superhighway.walls.sh)** — no
wallet, no signup. Then add the tools to your agent: see the [README](./README.md).

---

Superhighway is Wall #001 of [walls.sh](https://walls.sh) — a directory of businesses AI
agents pay for. Honest note: these are young endpoints; the incumbents above are more mature.
The bet is that *how agents buy* is changing, and per-call/no-key is where that goes.
