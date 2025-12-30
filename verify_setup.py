"""Setup verification script for Binance Futures Trading Bot."""
import os
import sys


def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("✗ Python 3.8 or higher is required")
        print(f"  Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
    return True


def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import requests
        print(f"✓ requests library installed (version {requests.__version__})")
        return True
    except ImportError:
        print("✗ requests library not found")
        print("  Run: pip install -r requirements.txt")
        return False


def check_environment_variables():
    """Check if required environment variables are set."""
    required_vars = ["BINANCE_API_KEY", "BINANCE_API_SECRET"]
    optional_vars = ["BINANCE_TESTNET"]
    
    all_set = True
    
    for var in required_vars:
        value = os.getenv(var)
        if value:
            masked = value[:4] + "..." + value[-4:] if len(value) > 8 else "***"
            print(f"✓ {var} is set: {masked}")
        else:
            print(f"✗ {var} is not set")
            all_set = False
    
    for var in optional_vars:
        value = os.getenv(var, "true")
        print(f"✓ {var}: {value}")
    
    return all_set


def check_project_structure():
    """Check if all required files exist."""
    required_files = [
        "src/__init__.py",
        "src/binance_client.py",
        "src/config.py",
        "src/logger.py",
        "src/validators.py",
        "src/market_orders.py",
        "src/limit_orders.py",
        "src/advanced/__init__.py",
        "src/advanced/oco.py",
        "src/advanced/twap.py",
        "requirements.txt",
        "README.md"
    ]
    
    all_exist = True
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} not found")
            all_exist = False
    
    return all_exist


def test_api_connection():
    """Test connection to Binance API."""
    try:
        from src.binance_client import BinanceClient
        from src.config import config
        
        print(f"\n✓ Using {'testnet' if config.testnet else 'production'} environment")
        print(f"  Base URL: {config.base_url}")
        
        client = BinanceClient()
        
        # Try to get exchange info (public endpoint)
        print("\nTesting API connection...")
        info = client.get_exchange_info(symbol="BTCUSDT")
        
        if info and "symbols" in info:
            print("✓ Successfully connected to Binance API")
            print("✓ BTCUSDT symbol is available")
            return True
        else:
            print("✗ Unexpected API response")
            return False
            
    except ValueError as e:
        print(f"✗ Configuration error: {e}")
        return False
    except Exception as e:
        print(f"✗ API connection failed: {e}")
        return False


def main():
    """Run all verification checks."""
    print("=" * 60)
    print("Binance Futures Trading Bot - Setup Verification")
    print("=" * 60)
    
    print("\n[1/5] Checking Python version...")
    python_ok = check_python_version()
    
    print("\n[2/5] Checking dependencies...")
    deps_ok = check_dependencies()
    
    print("\n[3/5] Checking environment variables...")
    env_ok = check_environment_variables()
    
    print("\n[4/5] Checking project structure...")
    structure_ok = check_project_structure()
    
    print("\n[5/5] Testing API connection...")
    if env_ok and deps_ok:
        api_ok = test_api_connection()
    else:
        print("⊘ Skipping API test (dependencies or environment not ready)")
        api_ok = False
    
    print("\n" + "=" * 60)
    print("Verification Summary")
    print("=" * 60)
    
    checks = [
        ("Python Version", python_ok),
        ("Dependencies", deps_ok),
        ("Environment Variables", env_ok),
        ("Project Structure", structure_ok),
        ("API Connection", api_ok)
    ]
    
    for check_name, status in checks:
        symbol = "✓" if status else "✗"
        print(f"{symbol} {check_name}")
    
    all_passed = all(status for _, status in checks)
    
    if all_passed:
        print("\n🎉 All checks passed! You're ready to start trading.")
        print("\nTry your first order:")
        print("  python -m src.market_orders BTCUSDT BUY 0.001")
    else:
        print("\n⚠ Some checks failed. Please fix the issues above.")
        print("\nFor help, see:")
        print("  - QUICKSTART.md for setup instructions")
        print("  - README.md for detailed documentation")
    
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
