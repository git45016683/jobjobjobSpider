'''
Author: your name
Date: 2021-04-23 11:16:10
LastEditTime: 2021-04-23 16:21:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \job\job\items.py
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    pay = scrapy.Field()
    place = scrapy.Field()
    edu_v = scrapy.Field()
    experience = scrapy.Field()
    company = scrapy.Field()
