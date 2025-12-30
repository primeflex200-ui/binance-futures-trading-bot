#!/usr/bin/env python3
"""
Standalone entry point for limit orders.
Run with: python limit_order.py BTCUSDT SELL 0.01 42000
"""
import sys
import os

# Add src to path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Now we can import without the relative import issues
import limit_orders

if __name__ == "__main__":
    limit_orders.main()
