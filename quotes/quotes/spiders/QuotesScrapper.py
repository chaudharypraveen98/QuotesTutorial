import scrapy

from ..items import QuotesItem


class QuotesScraper(scrapy.Spider):
    name = "QuotesScraper"
    start_urls = ["https://www.goodreads.com/quotes/tag/inspirational"]

    def _parse(self, response, **kwargs):
        item = QuotesItem()
        for quote in response.css(".quote"):
            title = quote.css(".quoteText::text").extract_first()
            author = quote.css(".authorOrTitle::text").extract_first()
            item["title"] = title
            item["author"] = author
            # yield {
            #     "title": title
            # }
            yield item
