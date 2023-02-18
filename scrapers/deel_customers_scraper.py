import requests
from bs4 import BeautifulSoup

from data import Customer

URL = "https://deel.com"


def deel_customers_scraper() -> list[Customer]:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html5lib")
    logo_scroll = soup.find("div", class_="logo-scroll-inner")
    customer_divs = logo_scroll.find_all("div", class_="single-image")
    return [_parse_div(div) for div in customer_divs]


def _parse_div(customer_div):
    image_elements = customer_div.find("img")
    logo = image_elements["src"]
    name = image_elements["alt"]
    name = name.partition("_")[0]
    name = name.partition("-")[0]
    return Customer(
        logo_url=logo,
        name=name
    )
