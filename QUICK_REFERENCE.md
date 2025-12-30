# Quick Reference Card

## Setup (One-Time)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set environment variables (Windows CMD)
set BINANCE_API_KEY=your_testnet_key
set BINANCE_API_SECRET=your_testnet_secret
set BINANCE_TESTNET=true

# 3. Verify setup
python verify_setup.py
```

## Commands

### Market Orders
```bash
python -m src.market_orders <SYMBOL> <SIDE> <QUANTITY>

# Examples:
python -m src.market_orders BTCUSDT BUY 0.01
python -m src.market_orders ETHUSDT SELL 0.5
```

### Limit Orders
```bash
python -m src.limit_orders <SYMBOL> <SIDE> <QUANTITY> <PRICE>

# Examples:
python -m src.limit_orders BTCUSDT BUY 0.01 42000
python -m src.limit_orders ETHUSDT SELL 0.5 2500
```

### OCO Orders
```bash
python -m src.advanced.oco <SYMBOL> <SIDE> <QTY> <TP_PRICE> <SL_PRICE>

# Example:
python -m src.advanced.oco BTCUSDT BUY 0.01 45000 40000
```

### TWAP Strategy
```bash
python -m src.advanced.twap <SYMBOL> <SIDE> <TOTAL_QTY> <NUM_ORDERS> <INTERVAL>

# Example:
python -m src.advanced.twap BTCUSDT BUY 0.1 5 10
```

## Check Logs

```bash
# Windows
type bot.log

# Linux/Mac
cat bot.log
tail -f bot.log  # Follow in real-time
```

## Common Symbols

- `BTCUSDT` - Bitcoin
- `ETHUSDT` - Ethereum
- `BNBUSDT` - Binance Coin
- `SOLUSDT` - Solana
- `ADAUSDT` - Cardano

## Troubleshooting

| Error | Solution |
|-------|----------|
| Module not found | `pip install -r requirements.txt` |
| Environment variable required | Set BINANCE_API_KEY and BINANCE_API_SECRET |
| API request failed | Check API keys and internet connection |
| Invalid symbol | Use format: BTCUSDT (uppercase, no spaces) |
| Quantity must be positive | Use positive numbers only |

## Resources

- **Full Documentation**: README.md
- **Execution Guide**: EXECUTION_GUIDE.md
- **Quick Start**: QUICKSTART.md
- **Examples**: examples.md
- **Testnet**: https://testnet.binancefuture.com/
