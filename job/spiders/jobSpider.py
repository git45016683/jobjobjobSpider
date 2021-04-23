'''
Author: your name
Date: 2021-04-23 11:21:01
LastEditTime: 2021-04-23 11:38:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \job\job\spiders\jobSpider.py
'''
import scrapy


class JobspiderSpider(scrapy.Spider):
    name = 'jobSpider'
    allowed_domains = ['www.51job.com']
    start_urls = ['http://www.51job.com/']

    def parse(self, response):
        print(response)

