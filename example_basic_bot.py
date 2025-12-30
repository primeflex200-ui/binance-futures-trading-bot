"""Example usage of BasicBot class."""
import os
from src.basic_bot import BasicBot

# Initialize BasicBot with explicit testnet support
bot = BasicBot(
    api_key=os.getenv("BINANCE_API_KEY"),
    api_secret=os.getenv("BINANCE_API_SECRET"),
    testnet=True  # Explicitly use testnet
)

# Place a market order
response = bot.place_market_order("BTCUSDT", "BUY", 0.001)
print(f"Market order placed: {response}")

# Place a limit order
response = bot.place_limit_order("BTCUSDT", "SELL", 0.001, 50000)
print(f"Limit order placed: {response}")

# Get account info
account = bot.get_account_info()
print(f"Account balance: {account}")
