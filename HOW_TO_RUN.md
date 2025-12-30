# How to Run - Binance Futures Trading Bot

## For First-Time Users

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Get Testnet API Keys
1. Go to https://testnet.binancefuture.com/
2. Login with GitHub or email
3. Click "Generate HMAC_SHA256 Key"
4. Copy your API Key and Secret Key

### Step 3: Set Environment Variables

**Windows (Command Prompt):**
```cmd
set BINANCE_API_KEY=your_api_key_here
set BINANCE_API_SECRET=your_secret_key_here
set BINANCE_TESTNET=true
```

**Windows (PowerShell):**
```powershell
$env:BINANCE_API_KEY="your_api_key_here"
$env:BINANCE_API_SECRET="your_secret_key_here"
$env:BINANCE_TESTNET="true"
```

**Linux/Mac:**
```bash
export BINANCE_API_KEY="your_api_key_here"
export BINANCE_API_SECRET="your_secret_key_here"
export BINANCE_TESTNET="true"
```

### Step 4: Verify Setup
```bash
python verify_setup.py
```

If all checks pass, you're ready to trade!

## Running Commands

### Market Order (Buy Bitcoin)
```bash
python -m src.market_orders BTCUSDT BUY 0.001
```

**What happens:**
1. Bot connects to Binance Futures Testnet
2. Places market order to buy 0.001 BTC
3. Logs all details to `bot.log`
4. Shows order confirmation in terminal

**Expected output:**
```
✓ Market order placed successfully!
  Order ID: 12345678
  Symbol: BTCUSDT
  Side: BUY
  Quantity: 0.001
  Average Price: 42150.50
```

### Limit Order (Sell Bitcoin)
```bash
python -m src.limit_orders BTCUSDT SELL 0.001 45000
```

**What happens:**
1. Bot connects to Binance Futures Testnet
2. Places limit order to sell 0.001 BTC at $45,000
3. Order waits until price reaches $45,000
4. Logs all details to `bot.log`

**Expected output:**
```
✓ Limit order placed successfully!
  Order ID: 87654321
  Symbol: BTCUSDT
  Side: SELL
  Quantity: 0.001
  Price: 45000
  Status: NEW
```

## Alternative Execution Method

If module imports fail, use standalone scripts:

```bash
python run_market_order.py BTCUSDT BUY 0.001
python run_limit_order.py BTCUSDT SELL 0.001 45000
```

## Checking Logs

**View all logs:**
```bash
type bot.log          # Windows
cat bot.log           # Linux/Mac
```

**View last 20 lines:**
```bash
tail -20 bot.log      # Linux/Mac
Get-Content bot.log -Tail 20  # PowerShell
```

## Verifying Orders

1. Go to https://testnet.binancefuture.com/
2. Login with your account
3. Click "Orders" tab
4. Find your order by Order ID

## Common Issues

### "Module not found"
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### "Environment variable required"
**Solution:** Set environment variables (see Step 3 above)

### "API request failed"
**Solution:** 
- Check internet connection
- Verify API keys are correct
- Ensure BINANCE_TESTNET=true

## Command Syntax Reference

```bash
# Market Orders
python -m src.market_orders <SYMBOL> <SIDE> <QUANTITY>

# Limit Orders
python -m src.limit_orders <SYMBOL> <SIDE> <QUANTITY> <PRICE>

# OCO Orders
python -m src.advanced.oco <SYMBOL> <SIDE> <QTY> <TP_PRICE> <SL_PRICE>

# TWAP Strategy
python -m src.advanced.twap <SYMBOL> <SIDE> <TOTAL_QTY> <NUM_ORDERS> <INTERVAL_SEC>
```

## Parameters Explained

- **SYMBOL**: Trading pair (e.g., BTCUSDT, ETHUSDT)
- **SIDE**: BUY or SELL
- **QUANTITY**: Amount to trade (e.g., 0.001, 0.01, 1.0)
- **PRICE**: Limit price for limit orders (e.g., 42000, 45000)
- **TP_PRICE**: Take-profit price for OCO orders
- **SL_PRICE**: Stop-loss price for OCO orders
- **NUM_ORDERS**: Number of orders for TWAP
- **INTERVAL_SEC**: Seconds between TWAP orders

## More Examples

```bash
# Buy 0.01 BTC at market price
python -m src.market_orders BTCUSDT BUY 0.01

# Sell 0.5 ETH at market price
python -m src.market_orders ETHUSDT SELL 0.5

# Buy 0.01 BTC at $40,000
python -m src.limit_orders BTCUSDT BUY 0.01 40000

# Sell 1 ETH at $2,500
python -m src.limit_orders ETHUSDT SELL 1 2500

# Buy with take-profit and stop-loss
python -m src.advanced.oco BTCUSDT BUY 0.01 45000 40000

# Split large order over time
python -m src.advanced.twap BTCUSDT BUY 0.1 5 10
```

## Need More Help?

- **Quick Reference**: See QUICK_REFERENCE.md
- **Full Documentation**: See README.md
- **Detailed Guide**: See EXECUTION_GUIDE.md
- **Examples**: See examples.md
- **Troubleshooting**: See README.md troubleshooting section

## Safety Reminders

✅ Always use testnet first (BINANCE_TESTNET=true)
✅ Start with small amounts (0.001 BTC)
✅ Check logs after each order
✅ Verify orders on testnet interface
✅ Never commit API keys to version control

---

**You're ready to start trading! Begin with small test orders on testnet.**
