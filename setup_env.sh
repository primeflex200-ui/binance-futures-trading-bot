#!/bin/bash
# Setup script for Linux/Mac users
# This script helps set environment variables for the trading bot

echo "========================================"
echo "Binance Futures Trading Bot Setup"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "Python is installed: $(python3 --version)"
echo

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo

# Prompt for API credentials
echo "Please enter your Binance API credentials:"
echo "(Get testnet keys from https://testnet.binancefuture.com/)"
echo

read -p "Enter your BINANCE_API_KEY: " API_KEY
read -p "Enter your BINANCE_API_SECRET: " API_SECRET
read -p "Use testnet? (true/false, default=true): " USE_TESTNET

USE_TESTNET=${USE_TESTNET:-true}

echo
echo "Setting environment variables for this session..."
export BINANCE_API_KEY="$API_KEY"
export BINANCE_API_SECRET="$API_SECRET"
export BINANCE_TESTNET="$USE_TESTNET"

echo
echo "========================================"
echo "Environment variables set!"
echo "========================================"
echo "BINANCE_API_KEY: ${API_KEY:0:4}...${API_KEY: -4}"
echo "BINANCE_API_SECRET: ${API_SECRET:0:4}...${API_SECRET: -4}"
echo "BINANCE_TESTNET: $USE_TESTNET"
echo

echo "NOTE: These variables are only set for this terminal session."
echo "To make them permanent, add them to your ~/.bashrc or ~/.zshrc"
echo

echo "Running setup verification..."
python3 verify_setup.py

echo
echo "========================================"
echo "Setup complete!"
echo "========================================"
echo
echo "Try your first order:"
echo "  python3 -m src.market_orders BTCUSDT BUY 0.001"
echo
echo "For more examples, see examples.md"
echo
