'''
Author: your name
Date: 2021-04-23 11:16:10
LastEditTime: 2021-04-25 16:37:59
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
        self.cu.execute('SELECT count(*) FROM job WHERE url = ?', [item['url']])
        already_exist = self.cu.fetchall()
        # print(already_exist[0][0])
        if (already_exist[0][0] == 0):
            insert_sql = 'insert into job (title, pay, place, edu_v, experience, company, url, job_info) values ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(item['title'], item['pay'], item['place'], item['edu_v'], item['experience'], item['company'], item['url'], item['job_info'])
            print(insert_sql)
            self.cu.execute(insert_sql)
            self.con.commit()
        else:
            print('this job already in the database')
        return item

    def spider_close(self, spider):
        self.con.close()
