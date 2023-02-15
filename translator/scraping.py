import json

import requests
from bs4 import BeautifulSoup

with open('data.json', 'r', encoding='utf-8') as data:
    headers = json.load(data)['headers']

# since we are making multiple requests to the
# same host, making requests from the Session instance
# can result in significant performance increase
session = requests.Session()


class Scraper:

    def __init__(self, source: str, target: str, word: str):
        self.source = source
        self.target = target
        self.word = word

    def _request_call(self) -> requests.Response:
        base_url = "https://context.reverso.net/translation/"
        # create the url
        url = base_url + f"{self.source}-{self.target}/{self.word}"

        try:
            # specifying the headers to make our request
            # present itself as some kind of browser
            response = session.get(url, headers=headers)
            return response
        except requests.exceptions.Timeout:  # timeout error
            raise SystemExit("Connection timed out. Please try again.")
        except requests.exceptions.RequestException:  # other possible errors
            raise SystemExit("Connection failed. Check your internet connection.")

    def scrape(self) -> tuple[list[str], list[str]]:
        response = self._request_call()
        soup = BeautifulSoup(response.content, 'html.parser')

        # scraping 3 translation result
        words = [tag.text for tag in soup.find_all(
                "span", {"class": "display-term"}, limit=3)]
        # scraping 2 example pairs (each pair: one in source lang, one in target lang)
        examples = [tag.text.strip() for tag in soup.find_all(
                    "div", {"class": ["src ltr", "trg ltr", "trg rtl", "trg rtl arabic"]},
                    limit=4)]

        return words, examples
