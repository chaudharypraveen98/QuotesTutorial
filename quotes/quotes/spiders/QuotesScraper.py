import scrapy

from ..items import QuotesItem


class QuotesScraper(scrapy.Spider):
    page_number = 2
    name = "QuotesScraper"
    start_urls = ["https://www.goodreads.com/quotes/tag/inspirational"]

    def _parse(self, response, **kwargs):
        item = QuotesItem()
        for quote in response.css(".quote")[:2]:
            title = quote.css(".quoteText::text").extract_first()
            author = quote.css(".authorOrTitle::text").extract_first()
            item["title"] = title
            item["author"] = author
            # yield {
            #     "title": title
            # }
            yield item
        # next_btn = response.css("a.next_page::attr(href)").get()
        # if next_btn is not None:
        #     yield response.follow(next_btn, callback=self._parse())
        next_page=f"https://www.goodreads.com/quotes/tag/inspirational?page={QuotesScraper.page_number}"
        next_page = f"https://www.goodreads.com/quotes/tag/inspirational?page={QuotesScraper.page_number}"
        if QuotesScraper.page_number < 3:
            QuotesScraper.page_number += 1
            yield response.follow(next_page, callback=self._parse)
