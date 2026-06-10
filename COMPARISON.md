# Web search for AI agents: Superhighway vs. the usual way

If you're giving an AI agent live web access — search and reading pages — the usual way
is a search API or scraping API built for a **human**: sign up, get an API key, store the
secret, put a card on file, commit to a plan.

[Superhighway](https://superhighway.walls.sh) is web search built for the **agent**: it
pays per call in USDC over HTTP (the [x402](https://x402.org) protocol). No signup, no
API key, no subscription, no dashboard. One `npx` line and your agent can search the live
web and read any page — paying for exactly what it uses.

## The difference that matters for agents

| | Superhighway | A typical key-and-card search/scraping API |
|---|---|---|
| **Signup / account** | None | Required |
| **API key** | None | Required (a human creates + rotates it) |
| **Pricing model** | Pay **per call** in USDC | Monthly plans / credit packs / committed tiers |
| **Minimum commitment** | $0 — pay for exactly what you use | Usually a plan or minimum |
| **Who can buy** | An **agent** with a wallet, autonomously | A human, via a signup funnel an agent can't navigate |
| **Settlement** | On-chain, ~12s, no chargebacks | Card on file / invoice |
| **Setup for an agent** | One MCP line (`npx -y superhighway-mcp`) | Provision key → store secret → wire SDK |

Superhighway isn't trying to out-feature mature search products. The wedge is the
**purchase model**: an agent can discover, pay for, and use it in one autonomous
round-trip, which a key-and-card API fundamentally can't offer.

## What you get (one install, the whole search job)

| Tool | What it does | Price/call |
|---|---|---|
| `web_search` | Live, ranked web results as clean JSON — aggregated across many engines, routes around throttling | $0.001 |
| `news_search` | Recent news articles with published dates, for time-sensitive questions | $0.001 |
| `scrape` | Read any URL → title + clean markdown + plain text (boilerplate stripped) | $0.002 |
| `research` | Search + read the top pages in ONE call — content, not links | $0.005 |

**Find it, read it, pay per call.** Search finds the right pages; scrape turns them into
content your agent can actually use — answers, summaries, RAG input. Or let `research` do
the whole job in a single call.

Prefer a key after all? There's also a [free API-key plan](https://superhighway.walls.sh/pricing)
(1,000 calls/month, no card) with paid tiers — same four tools, human-friendly billing.

## When to use which

- **Use Superhighway** when an autonomous agent needs live web answers *and you don't want
  to provision/rotate API keys or commit to a plan* — especially for many small agents,
  each paying for exactly what it uses.
- **Use a dedicated incumbent** when you need one capability at high scale with SLAs,
  enterprise support, or features beyond the basics. (You can use both.)

## Try it (free, no wallet)

Run a search in the box at **[superhighway.walls.sh](https://superhighway.walls.sh)** — no
wallet, no signup. Then add the tools to your agent: see the [README](./README.md).

---

Superhighway is Wall #001 of [walls.sh](https://walls.sh) — a directory of businesses AI
agents pay for. Honest note: this is a young product; mature search incumbents have more
features. The bet is that *how agents buy* is changing, and per-call/no-key is where that goes.
