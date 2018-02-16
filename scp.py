import requests
from bs4 import BeautifulSoup
import sys


def get_html(URL):
    requests
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
