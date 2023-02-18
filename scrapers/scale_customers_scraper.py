import requests
from bs4 import BeautifulSoup

from data import Customer

URL = "https://scale.com/customers"


def scale_customers_scraper() -> list[Customer]:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html5lib")
    customer_articles = soup.find_all("article")
    return [_parse_article(article) for article in customer_articles]


def _parse_article(article):
    return Customer(
        logo_url=_parse_logo(article),
        name=parse_name(article))


def _parse_logo(article):
    logo_element = _find_logo_img_element(article)
    if logo_element:
        return logo_element["src"]
    else:
        return None

def _find_logo_img_element(article):
    image_elements = article.find_all("img")
    for image_element in image_elements:
        if "logo" in image_element["alt"]:
            return image_element


def parse_name(article):
    logo_element = _find_logo_img_element(article)
    if logo_element:
        alt_text = logo_element["alt"].strip()
        text = alt_text.replace("Customer Success Story: ", "")
        text = text.partition(" | ")[0]
        return text
    else:
        return None
