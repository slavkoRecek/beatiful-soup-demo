import requests
from bs4 import BeautifulSoup

from data import Customer

URL = "https://scale.com/customers"


def scale_customers_scraper() -> list[Customer]:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html5lib")
    customer_articles = soup.find_all("article")
    logo, name = parse_article(customer_articles[0])
    Customer(name=name, logo_url=logo)
    customers = []
    for article in customer_articles:
        logo, name = parse_article(article)
        customers.append(Customer(name=name, logo_url=logo))
    return customers


def parse_article(article):
    return parse_logo(article), parse_name(article)


def parse_logo(article):
    logo_element = find_logo_img_element(article)
    if logo_element:
        return logo_element["src"]
    else:
        return None

def find_logo_img_element(article):
    image_elements = article.find_all("img")
    for image_element in image_elements:
        if "logo" in image_element["alt"]:
            return image_element


def parse_name(article):
    logo_element = find_logo_img_element(article)
    if logo_element:
        alt_text = logo_element["alt"].strip()
        text = alt_text.replace("Customer Success Story: ", "")
        text = text.partition(" | ")[0]
        return text
    else:
        return None
