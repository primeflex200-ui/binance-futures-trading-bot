#!/usr/bin/env python3
"""
Standalone entry point for market orders.
Run with: python market_order.py BTCUSDT BUY 0.01
"""
import sys
import os

# Add src to path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Now we can import without the relative import issues
import market_orders

if __name__ == "__main__":
    market_orders.main()
