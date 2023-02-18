import requests
from bs4 import BeautifulSoup

from data import Customer

URL = "https://webflow.com"


def webflow_customers_scraper() -> list[Customer]:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html5lib")
    logos_sections = soup.find("section", class_="cc-logos")
    first_image_div = logos_sections.find("div", class_="intro-logos_wrapper")
    customer_logos = first_image_div.find_all("img")
    return [_parse_image(image) for image in customer_logos]


def _parse_image(image_element):
    logo = image_element["src"]
    name = image_element["alt"]
    return Customer(
        logo_url=logo,
        name=name
    )
