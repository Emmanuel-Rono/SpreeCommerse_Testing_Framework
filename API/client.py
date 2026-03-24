import requests

from Core.config import Settings


class ApiClient:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.session = requests.Session()

    def get(self, path: str, **kwargs):
        url = self._url(path)
        return self.session.get(url, **kwargs)

    def post(self, path: str, **kwargs):
        url = self._url(path)
        return self.session.post(url, **kwargs)

    def _url(self, path: str) -> str:
        if path.startswith("http"):
            return path
        return f"{self.settings.api_base_url.rstrip('/')}/{path.lstrip('/')}"
