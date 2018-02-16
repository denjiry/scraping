import requests
from bs4 import BeautifulSoup


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


def get_pair_page(URL):
    html = get_html(URL)
    sp = soup(html)
    list_date = get_class_text(sp, "schedule")
    list_title = get_class_text(sp, "event_title")
    return list(zip(list_date, list_title))


def get_events(pages):
    date_event = []
    for url in pages:
        pairs = get_pair_page(url)
        date_event += pairs
    return date_event


def dump_events(events, filename):
    pass


def main():
    events = get_events(PAGEs)
    dump_events(events, "events.txt")


if __name__ == "__main__":
    main()
