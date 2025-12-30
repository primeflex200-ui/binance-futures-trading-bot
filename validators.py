"""
Input validation for CLI arguments.
Quick sanity checks before hitting the API.
"""
from typing import Tuple


def validate_symbol(symbol: str) -> str:
    """Check if symbol looks valid (e.g., BTCUSDT)."""
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string")
    
    symbol = symbol.upper().strip()
    
    if not symbol.isalnum():
        raise ValueError("Symbol must contain only letters and numbers (e.g., BTCUSDT)")
    
    if len(symbol) < 3:
        raise ValueError("Symbol too short - use format like BTCUSDT")
    
    return symbol


def validate_side(side: str) -> str:
    """Check if side is BUY or SELL."""
    if not side or not isinstance(side, str):
        raise ValueError("Side must be a non-empty string")
    
    side = side.upper().strip()
    
    if side not in ("BUY", "SELL"):
        raise ValueError("Side must be BUY or SELL")
    
    return side


def validate_quantity(quantity: str) -> float:
    """Check if quantity is a positive number."""
    try:
        qty = float(quantity)
    except (ValueError, TypeError):
        raise ValueError("Quantity must be a number")
    
    if qty <= 0:
        raise ValueError("Quantity must be positive")
    
    return qty


def validate_price(price: str) -> float:
    """Check if price is a positive number."""
    try:
        prc = float(price)
    except (ValueError, TypeError):
        raise ValueError("Price must be a number")
    
    if prc <= 0:
        raise ValueError("Price must be positive")
    
    return prc


def parse_market_order_args(args: list) -> Tuple[str, str, float]:
    """Parse CLI args for market orders."""
    if len(args) != 3:
        raise ValueError("Usage: python -m src.market_orders <SYMBOL> <SIDE> <QUANTITY>")
    
    symbol = validate_symbol(args[0])
    side = validate_side(args[1])
    quantity = validate_quantity(args[2])
    
    return symbol, side, quantity


def parse_limit_order_args(args: list) -> Tuple[str, str, float, float]:
    """Parse CLI args for limit orders."""
    if len(args) != 4:
        raise ValueError("Usage: python -m src.limit_orders <SYMBOL> <SIDE> <QUANTITY> <PRICE>")
    
    symbol = validate_symbol(args[0])
    side = validate_side(args[1])
    quantity = validate_quantity(args[2])
    price = validate_price(args[3])
    
    return symbol, side, quantity, price
