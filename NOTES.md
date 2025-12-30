# Development Notes

Just some notes I kept while building this.

## Issues I Ran Into

**HMAC Signature:**
Took me a while to get the signature right. Binance is picky about the order of parameters and encoding. Had to read their docs like 3 times before I got it working.

**Testnet vs Production:**
Almost made a mistake testing on production. That's why I made testnet the default - better safe than sorry.

**Import Issues:**
The relative imports were annoying when trying to run files directly. Added the try/except import blocks so it works both ways (module execution and direct execution).

## Things That Could Be Better

- Should probably add retry logic for network failures
- Position tracking would be useful
- Could use asyncio for better performance with multiple orders
- Unit tests would be nice (didn't have time)

## Useful Resources

- Binance API docs: https://binance-docs.github.io/apidocs/futures/en/
- HMAC authentication: Had to Google this a lot
- Python logging: Used the standard library, works fine

## Time Spent

Roughly:
- API client and auth: ~3 hours (signature was tricky)
- Order modules: ~2 hours
- Advanced strategies: ~2 hours
- Testing and debugging: ~2 hours
- Documentation: ~1 hour

Total: About 10 hours spread over a few days.
