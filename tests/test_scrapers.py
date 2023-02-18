from unittest import TestCase

from scrapers.deel_customers_scraper import deel_customers_scraper
from scrapers.scale_customers_scraper import scale_customers_scraper
from scrapers.webflow_customers_scraper import webflow_customers_scraper


class ScraperTestCase(TestCase):

    def test_scale_costumers_scraper(self):
        self._verify_costumer_result(scale_customers_scraper)

    def test_deel_costumers_scraper(self):
        self._verify_costumer_result(deel_customers_scraper)

    def test_webflow_costumers_scraper(self):
        self._verify_costumer_result(webflow_customers_scraper)

    def _verify_costumer_result(self, scraper):
        customers = scraper()

        self.assertIsNotNone(customers)
        self.assertTrue(len(customers) > 1)
        self.assertIsNotNone(customers[0].name)
        self.assertIsNotNone(customers[0].logo_url)
