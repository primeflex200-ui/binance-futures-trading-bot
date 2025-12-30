"""Binance USDT-M Futures Trading Bot"""
__version__ = "1.0.0"

from .basic_bot import BasicBot
from .binance_client import BinanceClient

__all__ = ["BasicBot", "BinanceClient"]
