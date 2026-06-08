// Minimal x402 client — call Superhighway directly, no MCP.
// An agent that can sign an x402 payment pays per call with its own wallet.
//
//   npm i x402-fetch viem
//   AGENT_PRIVATE_KEY=0x... X402_NETWORK=base node examples/agent.mjs "your query"
//
import { wrapFetchWithPayment, createSigner, decodeXPaymentResponse } from "x402-fetch";

const BASE = process.env.SUPERHIGHWAY_URL || "https://superhighway.walls.sh";
const NETWORK = process.env.X402_NETWORK || "base";
const KEY = process.env.AGENT_PRIVATE_KEY;
const query = process.argv.slice(2).join(" ") || "what is x402?";

if (!KEY) {
  console.error("Set AGENT_PRIVATE_KEY (a funded Base wallet) to pay per call.");
  process.exit(1);
}

const signer = await createSigner(NETWORK, KEY);
const pay = wrapFetchWithPayment(fetch, signer); // intercepts 402, pays, retries

// web_search; swap the path for /news, /scrape?url=, or /geocode?q=
const res = await pay(`${BASE}/search?q=${encodeURIComponent(query)}&limit=5`);
if (!res.ok) {
  console.error("Request failed:", res.status, await res.text());
  process.exit(1);
}

const receipt = res.headers.get("x-payment-response");
if (receipt) console.log("Paid on-chain:", decodeXPaymentResponse(receipt).transaction, "\n");

const data = await res.json();
console.log(JSON.stringify(data, null, 2));
