from data import Page


class Scraper:

    def __init__(self, page_name, scraping_function):
        self.page_name = page_name
        self.scraping_function = scraping_function

    def scrape(self) -> Page:
        page = Page(name=self.page_name, customers=[])
        print(f"Scraping {self.page_name} page...")
        page.customers = self.scraping_function()
        return page
