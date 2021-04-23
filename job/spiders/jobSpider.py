import scrapy


class JobspiderSpider(scrapy.Spider):
    name = 'jobSpider'
    allowed_domains = ['www.51job.com']
    start_urls = ['http://www.51job.com/']

    def parse(self, response):
        pass
