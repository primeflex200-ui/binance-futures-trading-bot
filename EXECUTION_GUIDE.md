# Execution Guide - Binance Futures Trading Bot

## Quick Reference

### Prerequisites Checklist
- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Testnet API keys obtained
- [ ] Environment variables set

### Command Syntax

```bash
# Market Orders
python -m src.market_orders <SYMBOL> <SIDE> <QUANTITY>

# Limit Orders
python -m src.limit_orders <SYMBOL> <SIDE> <QUANTITY> <PRICE>

# OCO Orders
python -m src.advanced.oco <SYMBOL> <SIDE> <QUANTITY> <TP_PRICE> <SL_PRICE>

# TWAP Strategy
python -m src.advanced.twap <SYMBOL> <SIDE> <TOTAL_QTY> <NUM_ORDERS> <INTERVAL_SEC>
```

## Step-by-Step Execution

### 1. First-Time Setup

**Install Python dependencies:**
```bash
pip install -r requirements.txt
```

**Get testnet API keys:**
1. Go to https://testnet.binancefuture.com/
2. Login and generate HMAC_SHA256 keys
3. Copy API Key and Secret

**Set environment variables:**

Windows CMD:
```cmd
set BINANCE_API_KEY=your_key_here
set BINANCE_API_SECRET=your_secret_here
set BINANCE_TESTNET=true
```

Windows PowerShell:
```powershell
$env:BINANCE_API_KEY="your_key_here"
$env:BINANCE_API_SECRET="your_secret_here"
$env:BINANCE_TESTNET="true"
```

Linux/Mac:
```bash
export BINANCE_API_KEY="your_key_here"
export BINANCE_API_SECRET="your_secret_here"
export BINANCE_TESTNET="true"
```

**Verify setup:**
```bash
python verify_setup.py
```

### 2. Execute Your First Order

**Market Order Example:**
```bash
python -m src.market_orders BTCUSDT BUY 0.001
```

**Expected Output:**
```
2024-12-30 10:30:45 - trading_bot - INFO - Binance client initialized - Testnet mode: True
2024-12-30 10:30:45 - trading_bot - INFO - Initiating market order: BTCUSDT BUY 0.001
2024-12-30 10:30:45 - trading_bot - INFO - Using Binance Futures - Testnet mode: True

✓ Market order placed successfully!
  Order ID: 12345678
  Symbol: BTCUSDT
  Side: BUY
  Quantity: 0.001
  Average Price: 42150.50
```

### 3. Check Logs

**View all logs:**
```bash
# Windows
type bot.log

# Linux/Mac
cat bot.log
```

**View last 20 lines:**
```bash
# Windows PowerShell
Get-Content bot.log -Tail 20

# Linux/Mac
tail -20 bot.log
```

**Follow logs in real-time:**
```bash
# Linux/Mac
tail -f bot.log
```

### 4. Verify on Testnet

1. Go to https://testnet.binancefuture.com/
2. Click "Orders" tab
3. Verify your order appears with correct details

## Common Execution Patterns

### Pattern 1: Quick Market Trade
```bash
# Buy immediately
python -m src.market_orders BTCUSDT BUY 0.01

# Check logs
type bot.log
```

### Pattern 2: Limit Order with Monitoring
```bash
# Place limit order
python -m src.limit_orders BTCUSDT BUY 0.01 40000

# Monitor logs
tail -f bot.log

# Check on testnet interface
```

### Pattern 3: Risk-Managed Trade (OCO)
```bash
# Enter position
python -m src.market_orders BTCUSDT BUY 0.01

# Set take-profit and stop-loss
python -m src.advanced.oco BTCUSDT BUY 0.01 45000 40000

# Verify both orders placed
type bot.log
```

### Pattern 4: Large Order Execution (TWAP)
```bash
# Split 0.1 BTC into 10 orders, 30 seconds apart
python -m src.advanced.twap BTCUSDT BUY 0.1 10 30

# Monitor progress (takes ~5 minutes)
tail -f bot.log
```

## Execution Checklist

Before each trade:
- [ ] Verify environment variables are set
- [ ] Check testnet mode is active
- [ ] Confirm symbol is correct (BTCUSDT, not BTC-USDT)
- [ ] Verify quantity is positive
- [ ] For limit orders, check price is reasonable
- [ ] Have testnet interface open for verification

After each trade:
- [ ] Check terminal output for success message
- [ ] Review bot.log for detailed execution info
- [ ] Verify order on testnet interface
- [ ] Confirm order ID matches

## Troubleshooting Execution

### Issue: "Module not found"
**Cause**: Dependencies not installed or wrong directory

**Solution**:
```bash
# Ensure you're in project root
cd path/to/project

# Install dependencies
pip install -r requirements.txt

# Try alternative execution
python run_market_order.py BTCUSDT BUY 0.01
```

### Issue: "Environment variable required"
**Cause**: API keys not set in current terminal

**Solution**:
```bash
# Re-set environment variables
set BINANCE_API_KEY=your_key
set BINANCE_API_SECRET=your_secret
set BINANCE_TESTNET=true

# Verify they're set (Windows)
echo %BINANCE_API_KEY%

# Verify they're set (Linux/Mac)
echo $BINANCE_API_KEY
```

### Issue: "API request failed"
**Cause**: Network issue, wrong keys, or API down

**Solution**:
1. Check internet connection
2. Verify API keys are correct
3. Ensure using testnet keys with BINANCE_TESTNET=true
4. Check Binance testnet status

### Issue: Order executes but not visible
**Cause**: Wrong environment (testnet vs production)

**Solution**:
1. Check bot.log for "Testnet mode: True"
2. Verify BINANCE_TESTNET=true
3. Check correct Binance interface (testnet vs production)

## Interview Talking Points

When explaining this bot in an interview:

### Architecture
- "The bot uses a modular architecture with separation of concerns"
- "BinanceClient handles all API communication with HMAC signature"
- "Validators ensure input sanitization before API calls"
- "Comprehensive logging provides audit trail"

### CLI Design
- "Uses sys.argv for argument parsing - simple and effective"
- "Clear error messages guide users to correct usage"
- "Terminal output shows key order details immediately"
- "Logs provide detailed information for debugging"

### Security
- "No hardcoded credentials - all from environment variables"
- "Testnet enabled by default for safety"
- "API keys never logged or exposed"
- "HMAC SHA256 signature for authenticated requests"

### Error Handling
- "Try-catch blocks at every API call"
- "Validation before API requests to fail fast"
- "User-friendly error messages in terminal"
- "Full stack traces in logs for debugging"

### Testing Strategy
- "Testnet support for safe testing"
- "verify_setup.py validates configuration"
- "Small order sizes recommended for initial testing"
- "Logs provide verification of execution"

## Production Considerations

Before using with real money:

1. **Thorough Testing**
   - Test all order types on testnet
   - Verify error handling works
   - Test with various symbols and quantities

2. **Security Hardening**
   - Set IP restrictions on API keys
   - Use separate API keys for production
   - Rotate keys regularly
   - Monitor API key usage

3. **Risk Management**
   - Start with small positions
   - Always use stop-losses
   - Monitor positions actively
   - Set position size limits

4. **Monitoring**
   - Set up log monitoring
   - Alert on errors
   - Track order execution
   - Monitor account balance

5. **Switch to Production**
   ```bash
   set BINANCE_TESTNET=false
   # Use production API keys
   ```

## Additional Resources

- **Binance Futures API Docs**: https://binance-docs.github.io/apidocs/futures/en/
- **Testnet Interface**: https://testnet.binancefuture.com/
- **Project README**: See README.md for complete documentation
- **Examples**: See examples.md for usage patterns

## Support

For issues:
1. Check bot.log for error details
2. Review this execution guide
3. Verify environment setup with verify_setup.py
4. Check README.md troubleshooting section
