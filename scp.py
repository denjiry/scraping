import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path


PAGEs = ["https://wbawakate.connpass.com/event/",
         "https://wbawakate.connpass.com/event/?page=2",
         "https://wbawakate.connpass.com/event/?page=3"]


def get_html(URL):
    resp = requests.get(URL)
    html_bytes = resp.content
    html = html_bytes.decode("utf-8")
    return html


def soup(html):
    soup = BeautifulSoup(html, "lxml")
    return soup


def get_class_text(soup, class_):
    list_xml = soup.find_all("p", attrs={"class": class_})
    list_text = [xml.text for xml in list_xml]
    return list_text


def clean_list_date(list_date):
    ret = []
    pattern = "201[78]/[01][0-9]/[0-3][0-9] *（.）"
    for dirty in list_date:
        match = re.search(pattern, dirty)
        if match is None:
            continue
        assert match is not None, "dirty: {}".format(dirty)
        ret.append(match.group(0))
    return ret


def get_pair_page(URL):
    html = get_html(URL)
    sp = soup(html)
    list_date = get_class_text(sp, "schedule")
    list_date = clean_list_date(list_date)
    list_title = get_class_text(sp, "event_title")
    return list(zip(list_date, list_title))


def get_events(pages):
    date_event = []
    for url in pages:
        pairs = get_pair_page(url)
        date_event += pairs
    return date_event


def dump_events(events, filename):
    isinstance(filename, Path)
    df = pd.DataFrame(events)
    df.to_csv(filename, header=["date", "event"], index=False)


def main():
    events = get_events(PAGEs)
    dump_events(events, Path("events.csv"))


if __name__ == "__main__":
    main()
