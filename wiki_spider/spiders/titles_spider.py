import scrapy

class TitlesSpider(scrapy.Spider):
    name = "titles"

    start_urls = [
        'https://en.wikipedia.org/wiki/Triangular_number',
        'https://en.m.wikipedia.org/wiki/Equilateral_triangle',
        'https://en.m.wikipedia.org/wiki/Geometry',
    ]

    def parse(self, response):
        page_title = response.css('h1::text').get()
        yield {'page_title': page_title}
