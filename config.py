"""
Configuration loaded from environment variables.
Keeps API keys out of the codebase.
"""
import os
from typing import Optional


class Config:
    """Reads config from environment - testnet is default for safety."""
    
    def __init__(self):
        self.api_key: Optional[str] = os.getenv("BINANCE_API_KEY")
        self.api_secret: Optional[str] = os.getenv("BINANCE_API_SECRET")
        # Default to testnet unless explicitly set to false
        self.testnet: bool = os.getenv("BINANCE_TESTNET", "true").lower() == "true"
        
    @property
    def base_url(self) -> str:
        """Get the right API endpoint based on testnet setting."""
        if self.testnet:
            return "https://testnet.binancefuture.com"
        return "https://fapi.binance.com"
    
    def validate(self) -> None:
        """Make sure we have the required API credentials."""
        if not self.api_key:
            raise ValueError("BINANCE_API_KEY environment variable is required")
        if not self.api_secret:
            raise ValueError("BINANCE_API_SECRET environment variable is required")


config = Config()
