import scrapy
from time import sleep


class Tesla(scrapy.Spider):
	name = "quotes"
	
	def start_request():

		urls = [
			'http://quotes.toscrape.com/page/1/',
			'http://quotes.toscrape.com/page/2/',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = 'quotes-%s.txt' % page

		with open(filename, 'w') as f:
			for quote in response.css(".quote span.text::text"):
				f.write(quote)
		self.log('Saved file {0}'.format(filename))

	

