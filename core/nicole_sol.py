import streamlit as st
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair
from solders.transaction import VersionedTransaction
import base58
import httpx
import base64

class SolanaEngine:
    def __init__(self, key_str):
        # NICOLE: Cleaning key sensors
        clean_key = key_str.strip().replace("O", "0")
        try:
            self.kp = Keypair.from_base58_string(clean_key)
            self.address = self.kp.pubkey()
            self.rpc = AsyncClient("https://api.mainnet-beta.solana.com")
        except Exception as e:
            st.error(f"NICOLE: Solana Engine Offline - {e}")
            self.kp = None

    async def get_balance(self):
        if not self.kp: return 0.0
        try:
            resp = await self.rpc.get_balance(self.address)
            return resp.value / 1_000_000_000
        except Exception:
            return 0.0

    async def execute_snipe(self, target_mint: str, amount_sol: float):
        """Swaps SOL for Token via Jupiter V6"""
        if not self.kp: return "NICOLE: Sensor Error"
        
        lamports = int(amount_sol * 1_000_000_000)
        
        async with httpx.AsyncClient() as client:
            try:
                # 1. Get Quote
                quote_url = f"https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint={target_mint}&amount={lamports}&slippageBps=100"
                quote_res = await client.get(quote_url)
                quote_data = quote_res.json()

                # 2. Get Swap Transaction
                swap_url = "https://quote-api.jup.ag/v6/swap"
                payload = {
                    "quoteResponse": quote_data,
                    "userPublicKey": str(self.address),
                    "wrapAndUnwrapSol": True
                }
                swap_res = await client.post(swap_url, json=payload)
                swap_data = swap_res.json()

                # 3. Sign and Send
                raw_tx = base64.b64decode(swap_data["swapTransaction"])
                tx = VersionedTransaction.from_bytes(raw_tx)
                
                # Sign
                signature = self.kp.sign_message(tx.message.serialize())
                
                result = await self.rpc.send_raw_transaction(bytes(tx))
                return f"SUCCESS: Tx Sig {result.value}"
            except Exception as e:
                return f"FAILURE: {str(e)}"
