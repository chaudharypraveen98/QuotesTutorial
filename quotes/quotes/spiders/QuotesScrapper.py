import scrapy

class QuotesScraper(scrapy.Spider):
    name = "QuotesScraper"
    start_urls = ["https://www.goodreads.com/quotes/tag/inspirational"]

    def _parse(self, response, **kwargs):
        title = response.css(".quoteText::text")[0].extract()
        yield {
            "title":title
        }