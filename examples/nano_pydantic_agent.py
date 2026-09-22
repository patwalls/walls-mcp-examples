"""
Pay for Superhighway's web tools with Nano (XNO) instead of USDC.

Superhighway settles per call over x402. x402 is rail-agnostic: the server names
the schemes it accepts in the `accepts[]` array of the 402 quote. Today
superhighway.walls.sh lists `eip155:8453/USDC`; if it also listed a Nano scheme
(e.g. `nano:mainnet`), any agent with only a Nano wallet could pay the same
sub-cent prices with zero fee and sub-second finality — no Base wallet, no USDC,
no gas token.

This example shows the agent side of that handshake. It reuses `feeless402`
(a self-custodied Nano x402 client from the Nano ecosystem) as the payment
building block, so nothing here reimplements wallets or signing.

    pip install feeless402
    nano-pay init                 # creates a self-custodied ~/.nano-pay wallet
    python examples/nano_pydantic_agent.py

NOTE: this is the *pattern*, not a live payment. Run it only against an endpoint
that accepts a Nano x402 scheme. superhighway.walls.sh does not accept Nano yet —
request it in the repo's issues (this is the docs gap the PR fills).
"""

import asyncio
import subprocess

from pydantic_ai import Agent
from pydantic_ai.tools import Tool


def nano_paid_search(query: str) -> str:
    """Call Superhighway's /search endpoint, paying its x402 price in Nano."""
    url = f"https://superhighway.walls.sh/search?q={query}&limit=5"
    # nano-pay pay does the whole x402 handshake with the local Nano wallet:
    # request -> parse the 402 quote -> price-cap check -> sign a send block
    # locally -> retry with PAYMENT-SIGNATURE + X-PAYMENT headers. See
    # https://github.com/Feeless402/feeless402
    try:
        return subprocess.run(
            ["nano-pay", "pay", url, "--max-xno", "0.05"],
            capture_output=True,
            text=True,
            timeout=120,
        ).stdout
    except FileNotFoundError:
        return "nano-pay is not installed (pip install feeless402)."
    except subprocess.TimeoutExpired:
        return "nano-pay timed out."


async def main() -> None:
    agent = Agent(
        "openai:gpt-4o-mini",
        tools=[
            Tool(
                nano_paid_search,
                name="nano_paid_search",
                description=(
                    "Search the web via Superhighway and pay the per-call price in "
                    "Nano. Returns ranked results as JSON."
                ),
            )
        ],
    )

    result = await agent.run(
        "Use nano_paid_search to find the latest on the x402 protocol "
        "and share the top result."
    )
    print(result.data)


if __name__ == "__main__":
    asyncio.run(main())
