# Usage Examples

Comprehensive examples for all trading bot features.

## Prerequisites

Before running any examples, ensure:
1. Environment variables are set (see QUICKSTART.md)
2. You're using testnet for practice
3. You have test funds in your testnet account

## Basic Examples

### Market Orders

**Buy Bitcoin at market price:**
```bash
python -m src.market_orders BTCUSDT BUY 0.001
```

**Sell Ethereum at market price:**
```bash
python -m src.market_orders ETHUSDT SELL 0.1
```

**Buy Solana at market price:**
```bash
python -m src.market_orders SOLUSDT BUY 1.0
```

### Limit Orders

**Buy Bitcoin at $40,000:**
```bash
python -m src.limit_orders BTCUSDT BUY 0.001 40000
```

**Sell Bitcoin at $50,000:**
```bash
python -m src.limit_orders BTCUSDT SELL 0.001 50000
```

**Buy Ethereum at $2,500:**
```bash
python -m src.limit_orders ETHUSDT BUY 0.1 2500
```

## Advanced Examples

### OCO Orders (Take-Profit + Stop-Loss)

**Long position with risk management:**
```bash
# Entry: Buy 0.01 BTC
# Take-profit: $45,000 (10% gain)
# Stop-loss: $40,000 (5% loss)
python -m src.advanced.oco BTCUSDT BUY 0.01 45000 40000
```

**Short position with risk management:**
```bash
# Entry: Sell 0.01 BTC
# Take-profit: $40,000
# Stop-loss: $45,000
python -m src.advanced.oco BTCUSDT SELL 0.01 40000 45000
```

**Conservative ETH trade:**
```bash
# Tight stop-loss for risk management
python -m src.advanced.oco ETHUSDT BUY 0.5 2800 2600
```

### TWAP Strategy

**Small order - 5 splits:**
```bash
# Buy 0.05 BTC total
# Split into 5 orders of 0.01 BTC each
# 10 seconds between orders
python -m src.advanced.twap BTCUSDT BUY 0.05 5 10
```

**Medium order - 10 splits:**
```bash
# Buy 1.0 ETH total
# Split into 10 orders of 0.1 ETH each
# 30 seconds between orders
python -m src.advanced.twap ETHUSDT BUY 1.0 10 30
```

**Large order - 20 splits:**
```bash
# Sell 0.2 BTC total
# Split into 20 orders of 0.01 BTC each
# 60 seconds (1 minute) between orders
python -m src.advanced.twap BTCUSDT SELL 0.2 20 60
```

**Fast execution:**
```bash
# Buy 0.1 BTC in 10 orders, 5 seconds apart
# Total execution time: ~45 seconds
python -m src.advanced.twap BTCUSDT BUY 0.1 10 5
```

## Real-World Scenarios

### Scenario 1: Day Trading Setup

**Step 1: Enter position with market order**
```bash
python -m src.market_orders BTCUSDT BUY 0.01
```

**Step 2: Set take-profit and stop-loss**
```bash
# Assuming entry at $42,000
# TP: $43,000 (2.4% gain)
# SL: $41,500 (1.2% loss)
python -m src.advanced.oco BTCUSDT BUY 0.01 43000 41500
```

### Scenario 2: Accumulation Strategy

**Accumulate Bitcoin over 1 hour:**
```bash
# Buy 0.1 BTC total
# 12 orders over 60 minutes (5 minutes apart)
python -m src.advanced.twap BTCUSDT BUY 0.1 12 300
```

### Scenario 3: Swing Trading

**Step 1: Place limit buy order**
```bash
# Wait for price to drop to support level
python -m src.limit_orders BTCUSDT BUY 0.02 41000
```

**Step 2: After fill, set exit orders**
```bash
# TP at resistance, SL below support
python -m src.advanced.oco BTCUSDT BUY 0.02 44000 40500
```

### Scenario 4: Scaling Out

**Exit large position gradually:**
```bash
# Sell 0.5 BTC over 30 minutes
# 15 orders, 2 minutes apart
python -m src.advanced.twap BTCUSDT SELL 0.5 15 120
```

## Testing Workflow

### 1. Verify Setup
```bash
python verify_setup.py
```

### 2. Test with Minimum Quantity
```bash
# Start with smallest possible order
python -m src.market_orders BTCUSDT BUY 0.001
```

### 3. Check Logs
```bash
# Windows
type bot.log

# Linux/Mac
cat bot.log
```

### 4. Verify on Testnet
- Login to https://testnet.binancefuture.com/
- Check "Orders" and "Positions" tabs
- Verify order execution

## Common Patterns

### Pattern 1: Quick Scalp
```bash
# Fast in and out
python -m src.market_orders BTCUSDT BUY 0.01
python -m src.limit_orders BTCUSDT SELL 0.01 42500
```

### Pattern 2: Dollar-Cost Averaging
```bash
# Buy same amount every day
python -m src.market_orders BTCUSDT BUY 0.001
# Run daily via scheduler
```

### Pattern 3: Breakout Trade
```bash
# Buy on breakout
python -m src.market_orders BTCUSDT BUY 0.02
# Immediate stop-loss
python -m src.advanced.oco BTCUSDT BUY 0.02 45000 41800
```

## Error Handling Examples

### Invalid Symbol
```bash
python -m src.market_orders INVALID BUY 0.01
# Output: ✗ Error: Symbol validation failed
```

### Invalid Quantity
```bash
python -m src.market_orders BTCUSDT BUY -0.01
# Output: ✗ Error: Quantity must be positive
```

### Missing Arguments
```bash
python -m src.limit_orders BTCUSDT BUY
# Output: ✗ Usage: python limit_orders.py <SYMBOL> <SIDE> <QUANTITY> <PRICE>
```

## Tips for Success

1. **Always test on testnet first**
2. **Start with small quantities**
3. **Monitor bot.log for details**
4. **Use TWAP for large orders to minimize slippage**
5. **Always set stop-losses with OCO orders**
6. **Verify orders on Binance interface**
7. **Keep API keys secure**

## Next Steps

- Review [README.md](README.md) for detailed documentation
- Check [QUICKSTART.md](QUICKSTART.md) for setup help
- Monitor logs in `bot.log` for all operations
- Experiment with different strategies on testnet
- When ready, switch to production with `BINANCE_TESTNET=false`

## Support

For issues or questions:
1. Check bot.log for error details
2. Review README.md troubleshooting section
3. Verify environment variables are set correctly
4. Ensure API keys have correct permissions
