"""
Demo mode - simulates trading without real API calls.
Perfect for learning and testing without risk.
"""
import sys
import random
from datetime import datetime


def simulate_market_order(symbol, side, quantity):
    """Simulate a market order execution."""
    # Generate fake but realistic data
    order_id = random.randint(10000000, 99999999)
    
    # Fake prices for common symbols
    prices = {
        "BTCUSDT": random.uniform(42000, 43000),
        "ETHUSDT": random.uniform(2200, 2300),
        "BNBUSDT": random.uniform(300, 320),
        "SOLUSDT": random.uniform(95, 105),
    }
    
    avg_price = prices.get(symbol, random.uniform(100, 1000))
    
    print(f"\n{'='*60}")
    print(f"DEMO MODE - No real money involved!")
    print(f"{'='*60}")
    print(f"\nSimulated market order executed successfully!")
    print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Order ID: {order_id}")
    print(f"  {side} {quantity} {symbol}")
    print(f"  Average Price: ${avg_price:,.2f}")
    print(f"  Total Value: ${avg_price * quantity:,.2f}")
    print(f"\nThis is a SIMULATION - no actual trade was placed")
    print(f"{'='*60}\n")


def simulate_limit_order(symbol, side, quantity, price):
    """Simulate a limit order placement."""
    order_id = random.randint(10000000, 99999999)
    
    print(f"\n{'='*60}")
    print(f"DEMO MODE - No real money involved!")
    print(f"{'='*60}")
    print(f"\nSimulated limit order placed successfully!")
    print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Order ID: {order_id}")
    print(f"  {side} {quantity} {symbol} @ ${price:,.2f}")
    print(f"  Status: NEW (waiting for price to reach ${price:,.2f})")
    print(f"  Total Value: ${price * quantity:,.2f}")
    print(f"\nThis is a SIMULATION - no actual trade was placed")
    print(f"{'='*60}\n")


def main():
    """Main entry point for demo mode."""
    if len(sys.argv) < 2:
        print("\nDemo Trading Bot - Usage:")
        print("  Market Order: python demo_mode.py market BTCUSDT BUY 0.01")
        print("  Limit Order:  python demo_mode.py limit BTCUSDT SELL 0.01 45000")
        print("\nExamples:")
        print("  python demo_mode.py market BTCUSDT BUY 0.01")
        print("  python demo_mode.py market ETHUSDT SELL 0.5")
        print("  python demo_mode.py limit BTCUSDT BUY 0.01 40000")
        print("  python demo_mode.py limit ETHUSDT SELL 1 2500\n")
        sys.exit(1)
    
    order_type = sys.argv[1].lower()
    
    try:
        if order_type == "market":
            if len(sys.argv) != 5:
                print("\nUsage: python demo_mode.py market <SYMBOL> <SIDE> <QUANTITY>")
                print("Example: python demo_mode.py market BTCUSDT BUY 0.01\n")
                sys.exit(1)
            
            symbol = sys.argv[2].upper()
            side = sys.argv[3].upper()
            quantity = float(sys.argv[4])
            
            if side not in ["BUY", "SELL"]:
                print("\nError: Side must be BUY or SELL\n")
                sys.exit(1)
            
            if quantity <= 0:
                print("\nError: Quantity must be positive\n")
                sys.exit(1)
            
            simulate_market_order(symbol, side, quantity)
            
        elif order_type == "limit":
            if len(sys.argv) != 6:
                print("\nUsage: python demo_mode.py limit <SYMBOL> <SIDE> <QUANTITY> <PRICE>")
                print("Example: python demo_mode.py limit BTCUSDT SELL 0.01 45000\n")
                sys.exit(1)
            
            symbol = sys.argv[2].upper()
            side = sys.argv[3].upper()
            quantity = float(sys.argv[4])
            price = float(sys.argv[5])
            
            if side not in ["BUY", "SELL"]:
                print("\nError: Side must be BUY or SELL\n")
                sys.exit(1)
            
            if quantity <= 0:
                print("\nError: Quantity must be positive\n")
                sys.exit(1)
            
            if price <= 0:
                print("\nError: Price must be positive\n")
                sys.exit(1)
            
            simulate_limit_order(symbol, side, quantity, price)
            
        else:
            print(f"\nError: Unknown order type '{order_type}'")
            print("Use 'market' or 'limit'\n")
            sys.exit(1)
            
    except ValueError as e:
        print(f"\nError: Invalid number format - {e}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
