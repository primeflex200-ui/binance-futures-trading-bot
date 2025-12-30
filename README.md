# Binance Futures Trading Bot

A CLI-based trading bot for Binance USDT-M Futures. Built this for learning how to interact with exchange APIs and practice building production-ready Python code.

## Why This Exists

I wanted to understand how trading bots work under the hood, so I built one from scratch. It's CLI-only because I wanted to focus on the core logic without dealing with UI frameworks. Plus, CLI tools are easier to automate and integrate into larger systems.

The bot uses Binance's testnet by default, which means you can test everything with fake money before risking anything real. This was a deliberate choice - I've seen too many horror stories of people accidentally running bots on production.

## What It Does

**Core Features:**
- Market orders (buy/sell immediately at current price)
- Limit orders (buy/sell when price reaches a specific level)
- OCO orders (one-cancels-other: set take-profit and stop-loss together)
- TWAP strategy (split large orders over time to reduce market impact)

Everything gets logged to `bot.log` so you can see exactly what happened. The logs include timestamps, order details, and full error traces when things go wrong.

## Setup

### Prerequisites

You'll need:
- Python 3.8 or higher
- A Binance Futures account (production, not testnet for this version)
- API keys from Binance

### Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Currently just needs `requests` for API calls. Kept dependencies minimal on purpose.

2. **Get API keys:**
- Go to https://binance.com/
- Navigate to API Management
- Create new API key with Futures permissions
- Copy the API key and secret
- Set IP restrictions for security

3. **Set environment variables:**

The bot reads credentials from environment variables (never hardcode API keys).

**Windows (CMD):**
```cmd
set BINANCE_API_KEY=your_api_key_here
set BINANCE_API_SECRET=your_api_secret_here
set BINANCE_TESTNET=false
```

**Windows (PowerShell):**
```powershell
$env:BINANCE_API_KEY="your_api_key_here"
$env:BINANCE_API_SECRET="your_api_secret_here"
$env:BINANCE_TESTNET="false"
```

**Linux/Mac:**
```bash
export BINANCE_API_KEY="your_api_key_here"
export BINANCE_API_SECRET="your_api_secret_here"
export BINANCE_TESTNET="false"
```

Note: Set `BINANCE_TESTNET=false` for production. The default is `true` for safety.

## Usage

### Market Orders

Buy or sell immediately at the current market price.

```bash
python -m src.market_orders BTCUSDT BUY 0.01
```

This will:
1. Connect to Binance
2. Place a market order to buy 0.01 BTC
3. Show you the order ID and execution price
4. Log everything to `bot.log`

**More examples:**
```bash
# Sell 0.5 ETH
python -m src.market_orders ETHUSDT SELL 0.5

# Buy 10 SOL
python -m src.market_orders SOLUSDT BUY 10
```

### Limit Orders

Place an order that only executes when the price reaches your target.

```bash
python -m src.limit_orders BTCUSDT BUY 0.01 40000
```

This places a buy order at $40,000. The order sits there until BTC drops to that price.

**More examples:**
```bash
# Sell 0.01 BTC when it hits $45,000
python -m src.limit_orders BTCUSDT SELL 0.01 45000

# Buy 1 ETH at $2,500
python -m src.limit_orders ETHUSDT BUY 1 2500
```

### OCO Orders (Advanced)

One-Cancels-Other orders let you set both a take-profit and stop-loss. When one executes, the other gets cancelled automatically.

```bash
python -m src.advanced.oco BTCUSDT BUY 0.01 45000 40000
```

This sets:
- Take profit at $45,000 (sell when price goes up)
- Stop loss at $40,000 (sell when price goes down)

**Important:** For BUY orders, take-profit must be higher than stop-loss. For SELL orders, it's the opposite.

Note: Binance Futures doesn't have true OCO, so these are placed as separate orders. You'd need to monitor and cancel manually if one fills.

### TWAP Strategy (Advanced)

Time-Weighted Average Price - splits a large order into smaller chunks executed over time. Useful for reducing market impact on big trades.

```bash
python -m src.advanced.twap BTCUSDT BUY 0.1 5 10
```

This will:
- Buy 0.1 BTC total
- Split into 5 orders of 0.02 BTC each
- Wait 10 seconds between each order

Takes about 40 seconds total to complete.

## Checking Logs

Everything gets logged to `bot.log` in the project root.

**View logs:**
```bash
# Windows
type bot.log

# Linux/Mac
cat bot.log
tail -f bot.log  # Follow in real-time
```

The logs show:
- When you connected (testnet or production)
- What order you tried to place
- The API response from Binance
- Any errors with full stack traces

## Project Structure

```
src/
├── binance_client.py    # Handles API calls and request signing
├── config.py            # Reads environment variables
├── logger.py            # Logging setup
├── validators.py        # Input validation
├── market_orders.py     # Market order execution
├── limit_orders.py      # Limit order execution
└── advanced/
    ├── oco.py          # OCO order logic
    └── twap.py         # TWAP strategy
```

Kept the structure simple - each file has one clear purpose. The `binance_client.py` handles all the API communication, including the HMAC signature that Binance requires for authenticated requests.

## Design Decisions

**Why CLI?**
- Easier to automate
- No UI framework dependencies
- Can be integrated into larger systems
- Forces you to think about the core logic

**Why environment variables?**
- Never commit API keys to git
- Easy to switch between different accounts
- Standard practice for production deployments

**Why minimal dependencies?**
- Only using `requests` for HTTP calls
- Less to maintain and update
- Easier to understand what's happening

## Common Issues

**"Module not found" error:**
```bash
pip install -r requirements.txt
```

**"Environment variable required" error:**
Make sure you've set `BINANCE_API_KEY` and `BINANCE_API_SECRET` in your current terminal session.

**"API request failed" error:**
- Check your internet connection
- Verify your API keys are correct
- Make sure you have IP restrictions set up properly
- Ensure you have funds in your Futures wallet

**"401 Unauthorized" error:**
- Check if your API key has Futures permissions enabled
- Verify IP restrictions are configured
- Make sure the API key is active

## Testing

I recommend starting with tiny amounts:

```bash
# Start small
python -m src.market_orders BTCUSDT BUY 0.001

# Check the logs
cat bot.log

# Verify on Binance interface
```

## What I Learned

Building this taught me:
- How exchange APIs work (authentication, rate limits, error handling)
- The importance of logging (saved me multiple times during debugging)
- Why input validation matters (Binance will reject bad requests anyway, but better to catch them early)
- How to structure a CLI application properly
- HMAC SHA256 signature generation for API security

## Future Ideas

Things I might add later:
- Position management (track open positions)
- More advanced strategies (DCA, grid trading)
- Better error recovery (retry logic for network issues)
- Configuration file support (in addition to env vars)
- WebSocket integration for real-time data

For now, keeping it simple and focused on the core functionality.

## Security Warning

⚠️ **Trading crypto is risky.** This bot is provided as-is for educational purposes. I'm not responsible if you lose money. Always:
- Test thoroughly first
- Start with small amounts
- Use stop-losses
- Don't invest more than you can afford to lose
- Understand what each command does before running it

## Resources

- [Binance Futures API Docs](https://binance-docs.github.io/apidocs/futures/en/)
- [Binance Futures Interface](https://www.binance.com/en/futures)

## License

MIT - do whatever you want with it.

## Usage

### Market Orders

Buy or sell immediately at the current market price.

```bash
python -m src.market_orders BTCUSDT BUY 0.01
```

This will:
1. Connect to Binance testnet
2. Place a market order to buy 0.01 BTC
3. Show you the order ID and execution price
4. Log everything to `bot.log`

**More examples:**
```bash
# Sell 0.5 ETH
python -m src.market_orders ETHUSDT SELL 0.5

# Buy 10 SOL
python -m src.market_orders SOLUSDT BUY 10
```

### Limit Orders

Place an order that only executes when the price reaches your target.

```bash
python -m src.limit_orders BTCUSDT BUY 0.01 40000
```

This places a buy order at $40,000. The order sits there until BTC drops to that price.

**More examples:**
```bash
# Sell 0.01 BTC when it hits $45,000
python -m src.limit_orders BTCUSDT SELL 0.01 45000

# Buy 1 ETH at $2,500
python -m src.limit_orders ETHUSDT BUY 1 2500
```

### OCO Orders (Advanced)

One-Cancels-Other orders let you set both a take-profit and stop-loss. When one executes, the other gets cancelled automatically.

```bash
python -m src.advanced.oco BTCUSDT BUY 0.01 45000 40000
```

This sets:
- Take profit at $45,000 (sell when price goes up)
- Stop loss at $40,000 (sell when price goes down)

**Important:** For BUY orders, take-profit must be higher than stop-loss. For SELL orders, it's the opposite.

### TWAP Strategy (Advanced)

Time-Weighted Average Price - splits a large order into smaller chunks executed over time. Useful for reducing market impact on big trades.

```bash
python -m src.advanced.twap BTCUSDT BUY 0.1 5 10
```

This will:
- Buy 0.1 BTC total
- Split into 5 orders of 0.02 BTC each
- Wait 10 seconds between each order

Takes about 40 seconds total to complete.

## Checking Logs

Everything gets logged to `bot.log` in the project root.

**View logs:**
```bash
# Windows
type bot.log

# Linux/Mac
cat bot.log
tail -f bot.log  # Follow in real-time
```

The logs show:
- When you connected (testnet or production)
- What order you tried to place
- The API response from Binance
- Any errors with full stack traces

## Project Structure

```
src/
├── binance_client.py    # Handles API calls and request signing
├── config.py            # Reads environment variables
├── logger.py            # Logging setup
├── validators.py        # Input validation
├── market_orders.py     # Market order execution
├── limit_orders.py      # Limit order execution
└── advanced/
    ├── oco.py          # OCO order logic
    └── twap.py         # TWAP strategy
```

Kept the structure simple - each file has one clear purpose. The `binance_client.py` handles all the API communication, including the HMAC signature that Binance requires for authenticated requests.

## Design Decisions

**Why CLI?**
- Easier to automate
- No UI framework dependencies
- Can be integrated into larger systems
- Forces you to think about the core logic

**Why testnet by default?**
- Safety first - you have to explicitly opt into production
- Free to test without risking real money
- Same API as production, so code works identically

**Why environment variables?**
- Never commit API keys to git
- Easy to switch between different accounts
- Standard practice for production deployments

**Why minimal dependencies?**
- Only using `requests` for HTTP calls
- Less to maintain and update
- Easier to understand what's happening

## Common Issues

**"Module not found" error:**
```bash
pip install -r requirements.txt
```

**"Environment variable required" error:**
Make sure you've set `BINANCE_API_KEY` and `BINANCE_API_SECRET` in your current terminal session.

**"API request failed" error:**
- Check your internet connection
- Verify your API keys are correct
- Make sure you're using testnet keys with `BINANCE_TESTNET=true`

**Order not showing up:**
- Check you're looking at the right interface (testnet vs production)
- Look at `bot.log` to see if the order actually went through
- Verify the order ID matches

## Testing

I recommend starting with tiny amounts on testnet:

```bash
# Start small
python -m src.market_orders BTCUSDT BUY 0.001

# Check the logs
cat bot.log

# Verify on testnet interface
# Go to testnet.binancefuture.com and check your orders
```

Once you're comfortable, you can increase the amounts or switch to production (but seriously, test thoroughly first).

## Production Use

To use with real money:

1. Get production API keys from Binance (not testnet)
2. Set `BINANCE_TESTNET=false`
3. Use your production keys

**Warning:** Trading crypto is risky. This bot is provided as-is for educational purposes. I'm not responsible if you lose money. Always:
- Test on testnet first
- Start with small amounts
- Use stop-losses
- Don't invest more than you can afford to lose

## What I Learned

Building this taught me:
- How exchange APIs work (authentication, rate limits, error handling)
- The importance of logging (saved me multiple times during debugging)
- Why input validation matters (Binance will reject bad requests anyway, but better to catch them early)
- How to structure a CLI application properly
- The value of testnet environments (made development way less stressful)

## Future Ideas

Things I might add later:
- Position management (track open positions)
- More advanced strategies (DCA, grid trading)
- Better error recovery (retry logic for network issues)
- Configuration file support (in addition to env vars)

For now, keeping it simple and focused on the core functionality.

## Resources

- [Binance Futures API Docs](https://binance-docs.github.io/apidocs/futures/en/)
- [Testnet Interface](https://testnet.binancefuture.com/)

## License

MIT - do whatever you want with it.
