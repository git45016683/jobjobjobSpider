'''
Author: your name
Date: 2021-04-23 11:16:10
LastEditTime: 2021-04-23 17:04:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \job\job\pipelines.py
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

# title = ""
# pay = ""
# place = ""
# edu_v = ''
# experience = ''
# company = ""

class JobPipeline(object):
    def open_spider(self, spider):
        self.con = sqlite3.connect('jobdb.s3db')
        self.cu = self.con.cursor()

    def process_item(self, item, spider):
        # print(spider.name)
        insert_sql = 'insert into job (title, pay, place, edu_v, experience, company) values ("{}", "{}", "{}", "{}", "{}", "{}")'.format(item['title'], item['pay'], item['place'], item['edu_v'], item['experience'], item['company'])
        # print(insert_sql)
        self.cu.execute(insert_sql)
        self.con.commit()
        return item

    def spider_close(self, spider):
        self.con.close()
