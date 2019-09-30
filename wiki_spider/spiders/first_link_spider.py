# -*- coding: utf-8 -*-
import scrapy
import json
import re

language_articles = json.load(open('exclusions/language-articles.json'))["language_article_urls"]
writing_systems_articles = json.load(open('exclusions/writing-systems-articles.json'))["writing_systems_articles"]
misc = json.load(open('exclusions/misc.json'))["misc"]

urls_to_exclude = list(set(language_articles + writing_systems_articles + misc))

def is_separate_article (url) :
    pattern = re.compile("(^/wiki/)")
    if bool(pattern.match(url)):
        return True
    return False

def is_help_article (url) :
    pattern = re.compile("(^/wiki/Help:)")
    if bool(pattern.match(url)):
        return True
    return False
    
def is_file (url) :
    pattern = re.compile("(^/wiki/File:)")
    if bool(pattern.match(url)):
        return True
    return False

def is_suffix (url) :
    pattern = re.compile("(^/wiki/-)")
    if bool(pattern.match(url)):
        return True
    return False

def is_disambiguation (url) :
    pattern = re.compile("disambiguation")
    if bool(pattern.search(url)):
        return True
    return False

def get_first_valid(url_list):
    for url in url_list:
        if (url not in urls_to_exclude 
            and is_separate_article(url) 
            and not is_help_article(url) 
            and not is_file(url)
            and not is_suffix(url)
            and not is_disambiguation(url)
            ):
            return url


class FirstLinkSpider(scrapy.Spider):
    name = "firstlink"

    start_urls = [
        # 'https://en.wikipedia.org/wiki/Triangular_number',
        # 'https://en.wikipedia.org/wiki/Topological_manifold',
        # 'https://en.wikipedia.org/wiki/Lancaster%27s_chevauchée_of_1346',
        # 'https://en.wikipedia.org/wiki/Trouble_Maker_(duo)',
        # 'https://en.m.wikipedia.org/wiki/Equilateral_triangle',
        # 'https://en.m.wikipedia.org/wiki/Geometry',
        # 'https://en.wikipedia.org/wiki/David_Bushnell',
        # 'https://en.wikipedia.org/wiki/Kenya_Mitsuhashi',
        # 'https://en.wikipedia.org/wiki/Rhyacionia_hafneri',
        # 'https://en.wikipedia.org/wiki/Czech_Republic_at_the_2013_World_Championships_in_Athletics',
        # 'https://en.wikipedia.org/wiki/In_the_End_(album)',
        # 'https://en.wikipedia.org/wiki/Ancient_Greek_language',
        # 'https://en.wikipedia.org/wiki/Abdullah_Qureshi',
        # 'https://en.wikipedia.org/wiki/Moonbi',
        # 'https://en.wikipedia.org/wiki/My_First_Taste_of_Texas',
        # 'https://en.wikipedia.org/wiki/List_of_MeSH_codes_(B08)',
        # 'https://pl.wikipedia.org/wiki/Ballistic_Missile_Defense',
        # 'https://en.wikipedia.org/wiki/United_States_national_missile_defense',
        'https://en.wikipedia.org/wiki/Carl_Jung',
    ]


    def parse(self, response):
        page_title = response.css('h1::text').get()

        all_link_hrefs = response.css('div.mw-parser-output p a::attr(href)').getall()
        first_link_href = response.urljoin(get_first_valid(all_link_hrefs))

        yield {
            'page title': page_title,
            'first href': first_link_href,
            # 'all hrefs': all_link_hrefs
        }

        yield scrapy.Request(first_link_href, callback=self.parse)                
