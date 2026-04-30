# SpreeCommerce Testing Framework
An MVP automation testing framework for SpreeCommerce built with Python, Pytest, and Selenium.

## Overview
This project was built to improve the structure, maintainability, and reusability of test automation code. It combines UI, API, visual, and basic performance checks in one framework with shared configuration and reusable page objects.

## Current Coverage
- UI tests in `Tests/ui`
- API tests in `Tests/api`
- Visual regression checks in `Tests/visual`
- Basic performance checks in `Tests/perf`
- Shared configuration and driver setup in `Core/`

## Project Structure
```text
API/             API client and related helpers
Core/            Shared configuration, waits, driver setup, logging, paths
Locators/        UI locators
Services/        Page objects and service-layer actions
Tests/           UI, API, visual, and performance tests
Artifacts/       Screenshots and generated test artifacts
```

## Setup
1. Create and activate a virtual environment.
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies.
```powershell
python -m pip install -r requirements.txt
```

3. Create your local environment file.
```powershell
Copy-Item .env.example .env
```

4. Update `.env` with the values you need.

## Running Tests
Run the full smoke suite:

```powershell
python -m pytest -m smoke
```

Run by category:

```powershell
python -m pytest -m ui
python -m pytest -m api
python -m pytest -m visual
python -m pytest -m perf
```

Run with more detail:

```powershell
python -m pytest -v
```

## Configuration
Runtime settings are loaded from `.env` through `Core/config.py`.

Important settings include:
- `BASE_URL`
- `API_BASE_URL`
- `BROWSER`
- `HEADLESS`
- `IMPLICIT_WAIT`
- `EXPLICIT_WAIT`
- `TEST_USER_EMAIL`
- `TEST_USER_PASSWORD`

Use `.env.example` as the template for local setup.

## Notes
- Failure screenshots are saved under `Artifacts/screenshots`
- Visual tests create a baseline on first run and compare on the next run
- The framework is structured for extension as more scenarios are added

## MVP Status
This project is currently positioned as an MVP:
- core framework structure is in place
- main test layers are organized
- configuration is centralized
- the codebase is prepared for future refinement and test expansion
