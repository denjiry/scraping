import pytest
from scp import main


URL = "https://wbawakate.connpass.com/event/"


def test_main():
    main(URL)
