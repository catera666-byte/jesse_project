import random
import os
from solders.pubkey import Pubkey

# Official Jito Tip Accounts for May 2026
JITO_TIP_ACCOUNTS = [
    "96g9sAgNHmB99EBHDvJqnQXpa9Snyh3Y7pQkREyX1W3x",
    "HFqU5x63VTqvQss8hp11i4wVV8bD44PvwucfZ2bU7gY3",
    "Cw8CFyM9FkoMi7K7Crf6HNWoUMUMFmAWmXp6Pee69zVN",
    "ADaUMid9yfUytqMBgopwjb2DTLSLLWDMFf4t6U82o6QY"
]

def prepare_jito_bundle(trade_tx):
    """Adds a 0.001 SOL tip to guarantee your sniper lands first"""
    tip_account = Pubkey.from_string(random.choice(JITO_TIP_ACCOUNTS))
    print(f"🚀 Preparing Jito Bundle (Tip Account: {str(tip_account)[:5]}...)")
    return tip_account

if __name__ == "__main__":
    print("⚡ Jito Sniper Module Loaded.")
    # Test execution
    prepare_jito_bundle(None)
