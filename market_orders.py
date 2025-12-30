"""
Market order execution.
Buys or sells immediately at current market price.
"""
import sys
import traceback

# Handle both direct execution and module execution
try:
    from .binance_client import BinanceClient
    from .logger import logger
    from .validators import parse_market_order_args
except ImportError:
    from binance_client import BinanceClient
    from logger import logger
    from validators import parse_market_order_args


def place_market_order(symbol: str, side: str, quantity: float) -> None:
    """Execute a market order - fills immediately at best available price."""
    try:
        logger.info(f"Market order requested: {side} {quantity} {symbol}")
        
        client = BinanceClient()
        
        # Execute the order
        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type="MARKET",
            quantity=quantity
        )
        
        # Extract response details
        order_id = response.get("orderId")
        executed_qty = response.get("executedQty")
        avg_price = response.get("avgPrice", "N/A")
        
        logger.info(f"Order filled - ID: {order_id}, Qty: {executed_qty}, Avg Price: {avg_price}")
        
        # Show user-friendly output
        print(f"\nOrder placed successfully on {'testnet' if client.testnet else 'production'}")
        print(f"  Order ID: {order_id}")
        print(f"  {side} {executed_qty} {symbol}")
        print(f"  Average Price: {avg_price}\n")
        
    except ValueError as e:
        logger.error(f"Invalid input: {e}")
        print(f"\nError: {e}\n")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Order failed: {e}")
        logger.error(traceback.format_exc())
        print(f"\nSomething went wrong while placing the order - check logs for details\n")
        sys.exit(1)


def main():
    """Entry point when running as a script."""
    try:
        symbol, side, quantity = parse_market_order_args(sys.argv[1:])
        place_market_order(symbol, side, quantity)
    except ValueError as e:
        print(f"\n{e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
