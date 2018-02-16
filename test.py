import pytest
from scp import *


URL = "https://wbawakate.connpass.com/event/"
html_file = "index.html"


def test_soup():
    with open(html_file) as p:
        html = p.read()
    soup(html)


def test_main():
    main(URL)
