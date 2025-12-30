# Quick Start

Get the bot running in 5 minutes.

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Just needs `requests` for API calls.

## 2. Get Testnet Keys

1. Go to https://testnet.binancefuture.com/
2. Login (GitHub or email works)
3. Generate HMAC_SHA256 keys
4. Copy the API key and secret

## 3. Set Environment Variables

**Windows (CMD):**
```cmd
set BINANCE_API_KEY=your_key_here
set BINANCE_API_SECRET=your_secret_here
set BINANCE_TESTNET=true
```

**Windows (PowerShell):**
```powershell
$env:BINANCE_API_KEY="your_key_here"
$env:BINANCE_API_SECRET="your_secret_here"
$env:BINANCE_TESTNET="true"
```

**Linux/Mac:**
```bash
export BINANCE_API_KEY="your_key_here"
export BINANCE_API_SECRET="your_secret_here"
export BINANCE_TESTNET="true"
```

## 4. Run Your First Order

```bash
python -m src.market_orders BTCUSDT BUY 0.001
```

You should see:
```
Order placed successfully on testnet
  Order ID: 12345678
  BUY 0.001 BTCUSDT
  Average Price: 42150.50
```

## 5. Check the Logs

```bash
# Windows
type bot.log

# Linux/Mac
cat bot.log
```

## What's Next?

Try a limit order:
```bash
python -m src.limit_orders BTCUSDT SELL 0.001 50000
```

Or check out the full README for more features (OCO orders, TWAP strategy, etc).

## Troubleshooting

**"Module not found"** → Run `pip install -r requirements.txt`

**"Environment variable required"** → Make sure you set the API keys in your current terminal

**"API request failed"** → Check your internet and verify the API keys are correct

## Notes

- The bot uses testnet by default (fake money, safe to test)
- Everything gets logged to `bot.log`
- Start with small amounts (0.001 BTC) to test
- Verify orders on https://testnet.binancefuture.com/
