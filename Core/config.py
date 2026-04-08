import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    base_url: str
    browser: str
    headless: bool
    remote_url: Optional[str]
    implicit_wait: int
    explicit_wait: int
    api_base_url: str
    screenshots_dir: str
    artifacts_dir: str
    test_user_email: Optional[str]
    test_user_password: Optional[str]
    


def _get_bool(value: Optional[str], default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y"}


def load_settings() -> Settings:
    # Load .env if present; safe to call repeatedly.
    load_dotenv()

    base_url = os.getenv("BASE_URL", "https://demo.spreecommerce.org").rstrip("/")
    api_base_url = os.getenv("API_BASE_URL", f"{base_url}/api/v2/storefront")

    return Settings(
        base_url=base_url,
        browser=os.getenv("BROWSER", "chrome").lower(),
        headless=_get_bool(os.getenv("HEADLESS"), False),
        remote_url=os.getenv("REMOTE_URL") or None,
        implicit_wait=int(os.getenv("IMPLICIT_WAIT", "5")),
        explicit_wait=int(os.getenv("EXPLICIT_WAIT", "10")),
        api_base_url=api_base_url,
        screenshots_dir=os.getenv("SCREENSHOTS_DIR", "Artifacts/screenshots"),
        artifacts_dir=os.getenv("ARTIFACTS_DIR", "Artifacts"),
        test_user_email=os.getenv("TEST_USER_EMAIL"),
        test_user_password=os.getenv("TEST_USER_PASSWORD")
    )

