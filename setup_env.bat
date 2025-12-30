@echo off
REM Setup script for Windows users
REM This script helps set environment variables for the trading bot

echo ========================================
echo Binance Futures Trading Bot Setup
echo ========================================
echo.

echo This script will help you set up environment variables.
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo Python is installed.
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Prompt for API credentials
echo Please enter your Binance API credentials:
echo (Get testnet keys from https://testnet.binancefuture.com/)
echo.

set /p API_KEY="Enter your BINANCE_API_KEY: "
set /p API_SECRET="Enter your BINANCE_API_SECRET: "
set /p USE_TESTNET="Use testnet? (true/false, default=true): "

if "%USE_TESTNET%"=="" set USE_TESTNET=true

echo.
echo Setting environment variables for this session...
set BINANCE_API_KEY=%API_KEY%
set BINANCE_API_SECRET=%API_SECRET%
set BINANCE_TESTNET=%USE_TESTNET%

echo.
echo ========================================
echo Environment variables set!
echo ========================================
echo BINANCE_API_KEY: %API_KEY:~0,4%...%API_KEY:~-4%
echo BINANCE_API_SECRET: %API_SECRET:~0,4%...%API_SECRET:~-4%
echo BINANCE_TESTNET: %USE_TESTNET%
echo.

echo NOTE: These variables are only set for this command prompt session.
echo To make them permanent, you need to set them in System Properties.
echo.

echo Running setup verification...
python verify_setup.py

echo.
echo ========================================
echo Setup complete!
echo ========================================
echo.
echo Try your first order:
echo   python -m src.market_orders BTCUSDT BUY 0.001
echo.
echo For more examples, see examples.md
echo.

pause
