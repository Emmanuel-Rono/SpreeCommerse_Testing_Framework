# About SpreeCommerse_Testing_Framework
An automated framework built with Selenium + Python to test SpreeCommerce.

## What this repo now includes
- UI tests (`Tests/ui`) using page/service objects
- API tests (`Tests/api`) using a shared API client
- Visual regression tests (`Tests/visual`) with baseline screenshots
- Performance checks (`Tests/perf`) with simple response time assertions
- Central config + driver factory under `Core/`

## Quick start
1) Install deps
```
python -m pip install -r requirements.txt
```
2) Configure environment
- Copy `.env.example` to `.env` and edit values as needed.

3) Run tests
```
pytest -m smoke
pytest -m ui
pytest -m api
pytest -m visual
pytest -m perf
```

## Notes for learning
- `Core/config.py` shows how we centralize settings for any test type.
- `Tests/conftest.py` wires fixtures and attaches screenshots on failures.
- `API/client.py` is a reusable HTTP layer for API tests.
- Visual tests create a baseline on first run and compare on re-run.
