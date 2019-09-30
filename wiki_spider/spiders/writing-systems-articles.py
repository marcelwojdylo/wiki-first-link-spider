# -*- coding: utf-8 -*-
import scrapy
import re

class WritingSystemsArticles(scrapy.Spider):
    name = "writing-systems-articles"

    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_writing_systems'
    ]

    def parse(self, response):

        urls = response.css('ul a::attr(href)').getall();

        def is_separate_article (url) :
            pattern = re.compile("(^/wiki/)")
            if bool(pattern.match(url)):
                return True
            return False

        writing_systems_article_urls = filter(is_separate_article, urls)


        return {
            'writing_systems_articles': writing_systems_article_urls,
        }