import pytest
from scp import soup, get_html


URL = "https://wbawakate.connpass.com/event/"
html_file = "index.html"


def test_get_html():
    html = get_html(URL)
    assert isinstance(html, str), "html isn't str: {}".format(type(html))
    return html


def test_soup():
    with open(html_file) as p:
        html = p.read()
    sp = soup(html)
    return sp
