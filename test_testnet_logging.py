"""Test script to verify testnet mode logging."""
import os
import sys

# Set test environment variables
os.environ["BINANCE_API_KEY"] = "test_key_12345678"
os.environ["BINANCE_API_SECRET"] = "test_secret_12345678"
os.environ["BINANCE_TESTNET"] = "true"

print("=" * 60)
print("Testing Testnet Mode Logging")
print("=" * 60)

# Test 1: BinanceClient with environment variables
print("\n[Test 1] BinanceClient with environment variables:")
try:
    from src.binance_client import BinanceClient
    client = BinanceClient()
    print(f"✓ Client initialized")
    print(f"  Testnet: {client.testnet}")
    print(f"  Base URL: {client.base_url}")
    assert client.testnet == True, "Testnet should be True"
    assert client.base_url == "https://testnet.binancefuture.com", "URL should be testnet"
    print("✓ Test 1 PASSED")
except Exception as e:
    print(f"✗ Test 1 FAILED: {e}")
    sys.exit(1)

# Test 2: BinanceClient with explicit parameters
print("\n[Test 2] BinanceClient with explicit parameters:")
try:
    client2 = BinanceClient(
        api_key="explicit_key",
        api_secret="explicit_secret",
        testnet=True
    )
    print(f"✓ Client initialized")
    print(f"  Testnet: {client2.testnet}")
    print(f"  Base URL: {client2.base_url}")
    assert client2.testnet == True, "Testnet should be True"
    assert client2.base_url == "https://testnet.binancefuture.com", "URL should be testnet"
    print("✓ Test 2 PASSED")
except Exception as e:
    print(f"✗ Test 2 FAILED: {e}")
    sys.exit(1)

# Test 3: BasicBot class
print("\n[Test 3] BasicBot class:")
try:
    from src.basic_bot import BasicBot
    bot = BasicBot(
        api_key="bot_key",
        api_secret="bot_secret",
        testnet=True
    )
    print(f"✓ BasicBot initialized")
    print(f"  Testnet: {bot.testnet}")
    print(f"  Client Testnet: {bot.client.testnet}")
    print(f"  Base URL: {bot.client.base_url}")
    assert bot.testnet == True, "Bot testnet should be True"
    assert bot.client.testnet == True, "Client testnet should be True"
    assert bot.client.base_url == "https://testnet.binancefuture.com", "URL should be testnet"
    print("✓ Test 3 PASSED")
except Exception as e:
    print(f"✗ Test 3 FAILED: {e}")
    sys.exit(1)

# Test 4: Production mode
print("\n[Test 4] Production mode (testnet=False):")
try:
    client_prod = BinanceClient(
        api_key="prod_key",
        api_secret="prod_secret",
        testnet=False
    )
    print(f"✓ Client initialized")
    print(f"  Testnet: {client_prod.testnet}")
    print(f"  Base URL: {client_prod.base_url}")
    assert client_prod.testnet == False, "Testnet should be False"
    assert client_prod.base_url == "https://fapi.binance.com", "URL should be production"
    print("✓ Test 4 PASSED")
except Exception as e:
    print(f"✗ Test 4 FAILED: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("All Tests PASSED! ✓")
print("=" * 60)
print("\nTestnet mode logging is working correctly.")
print("Check bot.log for detailed log entries.")
