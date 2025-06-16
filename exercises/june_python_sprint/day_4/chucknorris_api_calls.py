import sys
from urllib.parse import urljoin

import requests
from logger_utils import get_logger

log = get_logger("ChuckNorrisAPI")


class ChuckNorrisAPI:
    def __init__(self, base_url="https://api.chucknorris.io"):
        self.base_url = base_url
        self.session = requests.Session()  # reuse TCP connections for efficiency

        log.info(f"Initialized ChuckNorrisAPI client with base url: {self.base_url}")

    def _get(self, endpoint: str, params: dict = None) -> dict | None:
        """Internal helper to perform GET requests with error handling."""
        url = urljoin(self.base_url, endpoint)
        try:
            log.debug(f"Making GET request to URL: {url} with params: {params}")
            response = requests.get(url, params=params, timeout=5)  # 5 sec timeout
            response.raise_for_status()  # raises HTTPError for bad HTTP codes
            log.debug(f"Received response: {response.status_code} ")
            return response.json()
        except requests.exceptions.Timeout:
            log.error(f"Timeout while requesting {url}")
        except requests.exceptions.HTTPError as http_err:
            log.error(f"HTTP error occured: {http_err} - {response.text}")
        except requests.exceptions.RequestException as req_err:
            log.error(f"Request failed: {req_err}")
        except ValueError as json_err:
            log.error(f"JSON Decode error: {json_err}")
        return None  # Explicitly return None on failure

    def get_categories(self) -> list[str] | None:
        return self._get("/jokes/categories")

    def get_random_joke(self, category: str = None) -> dict | None:
        params = {"category": category} if category else None
        return self._get("/jokes/random", params=params)


if __name__ == "__main__":
    api_client = ChuckNorrisAPI()

    categories = api_client.get_categories()
    if categories:
        log.info(f"Available categories: {categories}")

        chosen_category = categories[0]
        joke = api_client.get_random_joke(chosen_category)
        if joke:
            log.info(f"Joke from category '{chosen_category}': {joke.get('value')}")
        else:
            log.warning("Failed to fetch joke")
    else:
        log.warning("Failed to fetch categories")
