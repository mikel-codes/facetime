# -*- coding: utf-8 -*-
import scrapy


class FacebookSpider(scrapy.Spider):
    name = 'facebook'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
    		'http://quotes.toscrape.com/page/1/',
			'http://quotes.toscrape.com/page/2/'
			]

    def parse(self, response):
    	try:
    		page = response.url.split("/")[-2]
    		filename = 'quotes-%s.txt' % page

    		with open(filename, 'w') as f:
    			for quote in response.css("div.quote"):
    				f.write(quote.css('span.text::text').get() + "\n\n")
    				f.write(quote.css('small.author::text').get() + "\n\n")
    				f.write(str([x for x in quote.css('div.tags a.tag::text').getall()]))
    				f.write("-----------------------------\n\n")


    	except Exception as e:
    		raise
    	else:
    		pass
    	finally:
    		pass

    	self.log('Saved file {0}'.format(filename))


