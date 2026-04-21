from binance.client import Client
import os

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():
    if not API_KEY or not API_SECRET:
        return None
    return Client(API_KEY, API_SECRET, testnet=True)