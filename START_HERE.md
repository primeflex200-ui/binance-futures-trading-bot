# 🚀 START HERE

Welcome to the Binance USDT-M Futures Trading Bot!

## What You Have

A professional, production-ready CLI trading bot with:
- ✅ Market & Limit orders
- ✅ OCO (Take-Profit + Stop-Loss) orders
- ✅ TWAP strategy for large orders
- ✅ Comprehensive logging
- ✅ Full input validation
- ✅ Testnet support

## Quick Start (5 Minutes)

### Option 1: Automated Setup (Recommended)

**Windows:**
```cmd
setup_env.bat
```

**Linux/Mac:**
```bash
chmod +x setup_env.sh
./setup_env.sh
```

### Option 2: Manual Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get testnet API keys:**
   - Visit: https://testnet.binancefuture.com/
   - Login and generate API keys

3. **Set environment variables:**
   
   Windows (CMD):
   ```cmd
   set BINANCE_API_KEY=your_key_here
   set BINANCE_API_SECRET=your_secret_here
   set BINANCE_TESTNET=true
   ```
   
   Linux/Mac:
   ```bash
   export BINANCE_API_KEY="your_key_here"
   export BINANCE_API_SECRET="your_secret_here"
   export BINANCE_TESTNET="true"
   ```

4. **Verify setup:**
   ```bash
   python verify_setup.py
   ```

5. **Place your first order:**
   ```bash
   python -m src.market_orders BTCUSDT BUY 0.001
   ```

## Documentation Guide

| Document | Purpose | When to Read |
|----------|---------|--------------|
| **START_HERE.md** | This file - quick orientation | First |
| **QUICKSTART.md** | 5-minute setup guide | Setup phase |
| **README.md** | Complete documentation | Reference |
| **examples.md** | Usage examples & patterns | Learning |
| **PROJECT_SUMMARY.md** | Technical overview | Understanding architecture |

## Your First Trade

After setup, try this:

```bash
# 1. Verify everything works
python verify_setup.py

# 2. Place a small market order
python -m src.market_orders BTCUSDT BUY 0.001

# 3. Check the logs
type bot.log          # Windows
cat bot.log           # Linux/Mac

# 4. Try a limit order
python -m src.limit_orders BTCUSDT SELL 0.001 50000
```

## Available Commands

### Basic Orders
```bash
# Market order
python -m src.market_orders <SYMBOL> <SIDE> <QUANTITY>

# Limit order
python -m src.limit_orders <SYMBOL> <SIDE> <QUANTITY> <PRICE>
```

### Advanced Orders
```bash
# OCO (Take-Profit + Stop-Loss)
python -m src.advanced.oco <SYMBOL> <SIDE> <QTY> <TP_PRICE> <SL_PRICE>

# TWAP (Split large orders)
python -m src.advanced.twap <SYMBOL> <SIDE> <TOTAL_QTY> <NUM_ORDERS> <INTERVAL_SEC>
```

## Project Structure

```
📁 project_root/
├── 📁 src/                    # Source code
│   ├── market_orders.py       # Market orders
│   ├── limit_orders.py        # Limit orders
│   ├── binance_client.py      # API client
│   ├── config.py              # Configuration
│   ├── logger.py              # Logging
│   ├── validators.py          # Input validation
│   └── 📁 advanced/
│       ├── oco.py             # OCO orders
│       └── twap.py            # TWAP strategy
├── 📄 bot.log                 # Execution logs
├── 📄 README.md               # Full documentation
├── 📄 QUICKSTART.md           # Quick setup
├── 📄 examples.md             # Usage examples
└── 📄 requirements.txt        # Dependencies
```

## Safety First! ⚠️

1. **Always use testnet first** (`BINANCE_TESTNET=true`)
2. **Start with tiny amounts** (0.001 BTC)
3. **Check bot.log** after each operation
4. **Never commit API keys** to version control
5. **Test thoroughly** before using real money

## Common Issues

**"Module not found"**
→ Run: `pip install -r requirements.txt`

**"Environment variable required"**
→ Set BINANCE_API_KEY and BINANCE_API_SECRET

**"API request failed"**
→ Check your API keys and internet connection

**Need more help?**
→ See README.md troubleshooting section

## Next Steps

1. ✅ Complete setup (above)
2. 📖 Read QUICKSTART.md for detailed setup
3. 🧪 Test with small orders on testnet
4. 📚 Explore examples.md for trading patterns
5. 📖 Review README.md for full documentation
6. 🚀 When ready, switch to production

## Support

- **Setup issues**: See QUICKSTART.md
- **Usage examples**: See examples.md
- **Full docs**: See README.md
- **Technical details**: See PROJECT_SUMMARY.md
- **Logs**: Check bot.log

## Ready to Trade?

```bash
# Verify your setup
python verify_setup.py

# If all checks pass, you're ready!
python -m src.market_orders BTCUSDT BUY 0.001
```

---

**Happy Trading! 📈**

Remember: This is a powerful tool. Use it responsibly and always manage your risk.
