"""
Limit order execution.
Places an order at a specific price - waits for market to reach that level.
"""
import sys
import traceback

# Handle both direct execution and module execution
try:
    from .binance_client import BinanceClient
    from .logger import logger
    from .validators import parse_limit_order_args
except ImportError:
    from binance_client import BinanceClient
    from logger import logger
    from validators import parse_limit_order_args


def place_limit_order(symbol: str, side: str, quantity: float, price: float) -> None:
    """Place a limit order - only executes if price is reached."""
    try:
        logger.info(f"Limit order requested: {side} {quantity} {symbol} @ {price}")
        
        client = BinanceClient()
        
        # Place the order
        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type="LIMIT",
            quantity=quantity,
            price=price,
            time_in_force="GTC"  # Good-Till-Cancel
        )
        
        order_id = response.get("orderId")
        status = response.get("status")
        
        logger.info(f"Limit order placed - ID: {order_id}, Status: {status}")
        
        print(f"\nLimit order placed on {'testnet' if client.testnet else 'production'}")
        print(f"  Order ID: {order_id}")
        print(f"  {side} {quantity} {symbol} @ {price}")
        print(f"  Status: {status}")
        print(f"  (Order will execute when price reaches {price})\n")
        
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
        symbol, side, quantity, price = parse_limit_order_args(sys.argv[1:])
        place_limit_order(symbol, side, quantity, price)
    except ValueError as e:
        print(f"\n{e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
