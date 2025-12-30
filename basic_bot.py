"""BasicBot class for simplified Binance Futures trading."""
from typing import Optional

from .binance_client import BinanceClient
from .logger import logger


class BasicBot:
    """
    Basic trading bot that wraps BinanceClient with simplified initialization.
    
    This class provides a clean interface for initializing the Binance Futures
    client with explicit testnet support.
    """
    
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        """
        Initialize the BasicBot with Binance credentials.
        
        Args:
            api_key: Binance API key
            api_secret: Binance API secret
            testnet: Whether to use testnet (default: True for safety)
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        
        # Initialize Binance client with explicit testnet support
        self.client = BinanceClient(
            api_key=api_key,
            api_secret=api_secret,
            testnet=testnet
        )
        
        logger.info(
            f"BasicBot initialized - "
            f"Testnet: {testnet}, "
            f"URL: {'https://testnet.binancefuture.com' if testnet else 'https://fapi.binance.com'}"
        )
    
    def place_market_order(self, symbol: str, side: str, quantity: float):
        """
        Place a market order.
        
        Args:
            symbol: Trading pair symbol
            side: Order side (BUY or SELL)
            quantity: Order quantity
            
        Returns:
            Order response from Binance API
        """
        return self.client.place_order(
            symbol=symbol,
            side=side,
            order_type="MARKET",
            quantity=quantity
        )
    
    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        """
        Place a limit order.
        
        Args:
            symbol: Trading pair symbol
            side: Order side (BUY or SELL)
            quantity: Order quantity
            price: Limit price
            
        Returns:
            Order response from Binance API
        """
        return self.client.place_order(
            symbol=symbol,
            side=side,
            order_type="LIMIT",
            quantity=quantity,
            price=price,
            time_in_force="GTC"
        )
    
    def get_account_info(self):
        """Get account information."""
        return self.client.get_account_info()
    
    def get_position_info(self, symbol: Optional[str] = None):
        """Get position information."""
        return self.client.get_position_info(symbol=symbol)
