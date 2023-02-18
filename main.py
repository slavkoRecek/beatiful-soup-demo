import dataclasses
import json

from data import Page
from scraper import Scraper
from scrapers.deel_customers_scraper import deel_customers_scraper
from scrapers.scale_customers_scraper import scale_customers_scraper
from scrapers.webflow_customers_scraper import webflow_customers_scraper


def scrape_pages():
    scraped_pages = []

    scale_scraper = Scraper(page_name='scale', scraping_function=scale_customers_scraper)
    scale_page: Page = scale_scraper.scrape()
    scraped_pages.append(scale_page)

    deel_scraper = Scraper(page_name='deel', scraping_function=deel_customers_scraper)
    deel_page: Page = deel_scraper.scrape()
    scraped_pages.append(deel_page)

    web_flow_scraper = Scraper(page_name='webflow', scraping_function=webflow_customers_scraper)
    web_flow_page: Page = web_flow_scraper.scrape()
    scraped_pages.append(web_flow_page)

    export_pages(scraped_pages)

    print("Finished scraping. Data exported to 'page_customers_info.json'.")


def export_pages(scraped_pages: list[Page]):
    with open("page_customers_info.json", "w") as json_file:
        pages_as_dict = [dataclasses.asdict(page) for page in scraped_pages]
        json_file.write(json.dumps(pages_as_dict, indent=4))


if __name__ == "__main__":
    scrape_pages()
