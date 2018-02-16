import requests
from bs4 import BeautifulSoup
import sys


def get_html(URL):
    resp = requests.get(URL)
    html_bytes = resp.content
    html = html_bytes.decode("utf-8")
    return html


def soup(html):
    soup = BeautifulSoup(html, "lxml")


def main(URL):
    html = get_html(URL)
    soup(html)


if __name__ == "__main__":
    URL = sys.argv[1]
    print("URL: ",URL)
    main(URL)
