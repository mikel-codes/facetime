# -*- coding: utf-8 -*-
import scrapy


class FacetimeSpider(scrapy.Spider):
    name = 'facetime'
    allowed_domains = ['facebook.com']
    start_urls = ['http://facebook.com/']

    def parse(self, response):
    	
        pass
