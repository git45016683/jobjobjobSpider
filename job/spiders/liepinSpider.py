import scrapy


class LiepinspiderSpider(scrapy.Spider):
    name = 'liepinSpider'
    allowed_domains = ['www.liepin.com']
    start_urls = ['http://www.liepin.com/']

    def parse(self, response):
        pass
