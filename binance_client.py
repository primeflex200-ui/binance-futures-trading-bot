"""
Binance Futures API client.
Handles authentication, request signing, and API calls.
"""
import hashlib
import hmac
import time
from typing import Any, Dict, Optional
from urllib.parse import urlencode

import requests

# Handle both direct execution and module execution
try:
    from .config import config
    from .logger import logger
except ImportError:
    from config import config
    from logger import logger


class BinanceClient:
    """
    Wrapper around Binance Futures API.
    Testnet is used by default for safety.
    """
    
    def __init__(self, api_key: Optional[str] = None, api_secret: Optional[str] = None, testnet: Optional[bool] = None):
        # Allow explicit credentials or fall back to env vars
        if api_key and api_secret:
            self.api_key = api_key
            self.api_secret = api_secret
            self.testnet = testnet if testnet is not None else config.testnet
            self.base_url = "https://testnet.binancefuture.com" if self.testnet else "https://fapi.binance.com"
        else:
            config.validate()
            self.api_key = config.api_key
            self.api_secret = config.api_secret
            self.testnet = config.testnet
            self.base_url = config.base_url
        
        logger.info(f"Connected to {'testnet' if self.testnet else 'production'} - {self.base_url}")
        
        self.session = requests.Session()
        self.session.headers.update({"X-MBX-APIKEY": self.api_key})
    
    def _generate_signature(self, params: Dict[str, Any]) -> str:
        """Generate HMAC SHA256 signature required by Binance."""
        query_string = urlencode(params)
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
    
    def _request(self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, signed: bool = False) -> Dict[str, Any]:
        """
        Internal method to make API calls.
        Handles signing for authenticated endpoints.
        """
        url = f"{self.base_url}{endpoint}"
        params = params or {}
        
        if signed:
            params["timestamp"] = int(time.time() * 1000)
            params["signature"] = self._generate_signature(params)
        
        try:
            response = self.session.request(method, url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Request to {endpoint} failed: {e}")
            # Try to log the actual error from Binance if available
            if hasattr(e, "response") and e.response is not None:
                try:
                    error_data = e.response.json()
                    logger.error(f"Binance error: {error_data}")
                except Exception:
                    logger.error(f"Response text: {e.response.text}")
            raise
    
    def get_exchange_info(self, symbol: Optional[str] = None) -> Dict[str, Any]:
        """
        Get exchange trading rules and symbol information.
        
        Args:
            symbol: Optional symbol to filter
            
        Returns:
            Exchange information
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._request("GET", "/fapi/v1/exchangeInfo", params=params)
    
    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, 
                    price: Optional[float] = None, time_in_force: str = "GTC", **kwargs) -> Dict[str, Any]:
        """
        Place an order on Binance Futures.
        This is the main method used by all order types.
        """
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            **kwargs
        }
        
        # Limit orders need a price
        if order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders")
            params["price"] = price
            params["timeInForce"] = time_in_force
        
        logger.info(f"Placing {order_type} order: {symbol} {side} {quantity}" + (f" @ {price}" if price else ""))
        response = self._request("POST", "/fapi/v1/order", params=params, signed=True)
        logger.info(f"Order placed - ID: {response.get('orderId')}")
        return response
    
    def get_account_info(self) -> Dict[str, Any]:
        """
        Get account information.
        
        Returns:
            Account information
        """
        return self._request("GET", "/fapi/v2/account", signed=True)
    
    def get_position_info(self, symbol: Optional[str] = None) -> Dict[str, Any]:
        """
        Get position information.
        
        Args:
            symbol: Optional symbol to filter
            
        Returns:
            Position information
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._request("GET", "/fapi/v2/positionRisk", params=params, signed=True)
