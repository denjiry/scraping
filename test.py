import pytest
from bs4 import BeautifulSoup


URL = "https://wbawakate.connpass.com/event/"
html_file = "index.html"
with open(html_file) as p:
        HTML = p.read()


def test_get_html():
    from scp import get_html
    html = get_html(URL)
    assert isinstance(html, str), "html isn't str: {}".format(type(html))
    return html


def test_soup():
    from scp import soup
    sp = soup(HTML)
    assert isinstance(sp, BeautifulSoup)
    return sp


def test_get_class_text():
    from scp import get_class_text
    sp = BeautifulSoup(HTML, "lxml")
    list_text = get_class_text(sp, "event_title")
    assert isinstance(list_text, list)
    assert isinstance(list_text[0], str)
    return list_text


def test_clean_list_date():
    from scp import clean_list_date
    dirty_list = ['\n終了\n      2018/01/13（土） 17:30〜\n      \n\n']
    clean_list = clean_list_date(dirty_list)
    assert clean_list == ["2018/01/13（土）"]
    return clean_list
