from bs4 import BeautifulSoup
import sys


def main(URL):
    with open(URL) as p:
        html = p.read()
    soup = BeautifulSoup(html, "lxml")


if __name__ == "__main__":
    URL = sys.argv[1]
    print("URL: ",URL)
    main(URL)
