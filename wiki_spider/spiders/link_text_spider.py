import scrapy

class LinkTextSpider(scrapy.Spider):
    name = "linktexts"

    start_urls = [
        'https://en.wikipedia.org/wiki/Triangular_number',
        'https://en.m.wikipedia.org/wiki/Equilateral_triangle',
        'https://en.m.wikipedia.org/wiki/Geometry',
    ]

    def parse(self, response):
        link_texts = response.css('div.mw-parser-output p a::text').getall()
        page_title = response.css('h1::text').get()
        yield {
            'page_title': page_title,
            'link_texts': link_texts
        }
