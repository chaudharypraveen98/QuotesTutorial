import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

from ..items import QuotesItem


class LoginQuoteScraper(scrapy.Spider):
    name = "LoginQuoteScraper"
    start_urls = ["http://quotes.toscrape.com/login"]

    def _parse(self, response, **kwargs):
        csrf_token = response.css("input[name='csrf_token']::attr(value)").extract_first()
        print(csrf_token)
        return FormRequest.from_response(response, formdata={
            "csrf_token": csrf_token,
            "username": "devil",
            "password": "password"
        }, callback=self.start_scraping, dont_filter=True)

    def start_scraping(self, response):
        open_in_browser(response)
        item = QuotesItem()
        for quote in response.css(".quote"):
            title = quote.css(".text::text").extract_first()
            author = quote.css(".author::text").extract_first()
            item["title"] = title
            item["author"] = author
            yield item
