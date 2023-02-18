import dataclasses
import json

from data import Page
from scrapers.scale_customers_scraper import scale_customers_scraper
from scraper import Scraper


def export_pages(scraped_pages: list[Page]):
    #        creates a json dump ot the scraped pages list into page_customers_info.json
    with open("page_customers_info.json", "w") as json_file:
        json_file.write(json.dumps([dataclasses.asdict(page) for page in scraped_pages]))


def create_scale_scraper():
    return Scraper(page_name='scale', scraping_function=scale_customers_scraper)


def scrape_pages():
    scraped_pages = []

    scale_scraper = create_scale_scraper()
    scale_page: Page = scale_scraper.scrape()
    scraped_pages.append(scale_page)

    export_pages(scraped_pages)


    print("Finished scraping. Data exported to 'page_customers_info.json'.")


if __name__ == "__main__":
    scrape_pages()