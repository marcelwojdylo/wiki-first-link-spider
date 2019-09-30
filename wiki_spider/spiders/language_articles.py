# -*- coding: utf-8 -*-
import scrapy
import re

class LanguageArticles(scrapy.Spider):
    name = "language-articles"

    start_urls = [
        'https://en.wikipedia.org/wiki/Index_of_language_articles'
    ]

    def parse(self, response):

        urls = response.css('table.sortable a::attr(href)').getall();

        def is_separate_article (url) :
            pattern = re.compile("(^/wiki/)")
            if bool(pattern.match(url)):
                return True
            return False

        language_article_urls = filter(is_separate_article, urls)


        return {
            'language_article_urls': language_article_urls,
        }