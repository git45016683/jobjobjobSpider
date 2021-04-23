'''
Author: your name
Date: 2021-04-23 11:21:01
LastEditTime: 2021-04-23 16:13:31
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \job\job\spiders\jobSpider.py
'''
import scrapy
from scrapy.utils.trackref import print_live_refs


class JobspiderSpider(scrapy.Spider):
    name = 'jobSpider'
    allowed_domains = ['www.51job.com']
    start_urls = ['https://www.51job.com', 'search.51job.com']
    # start_urls = ['https://search.51job.com/list/030000%252c030200,000000,2602%252c2609,01%252c37%252c02%252c31%252c33,9,09,%25E6%258A%2580%25E6%259C%25AF%25E7%25AE%25A1%25E7%2590%2586,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']
    start_urls = ['https://msearch.51job.com/job_list.php?keyword=%E6%8A%80%E6%9C%AF%E7%AE%A1%E7%90%86&keywordtype=2&jobarea=030000%2C030200&landmark=&issuedate=&saltype=09&degree=&funtype=2602%2C2609&indtype=&jobterm=&cotype=&workyear=&cosize=&lonlat=&line=&radius=&areaname=&from=&searchtype=&fromapp=&filttertype=']


    def parse(self, response):
        # print(response)
        job_div_list = response.xpath('//*[@id="pageContent"]/div[4]/a')
        # print(job_div_list)
        for div in job_div_list:
            title = ""
            pay = ""
            place = ""
            edu_v = ''
            experience = ''
            company = ""
            
            # 职位名称
            title = div.xpath('./strong/span/text()').extract()[0]
            # print(title)
            
            # 职位待遇
            pay = div.xpath('./i/text()').extract()[0]
            # print(pay)

            # 职位工作地点
            place = div.xpath('./em/text()').extract()[0]
            # print(place)

            # 工作学历要求/工作经验要求
            edu = div.xpath('./p/text()').extract()
            str = edu[0]
            
            if str.find('|') != -1:
                str_list = str.split('|')
                if len(str_list) > 2:
                    edu_v = str_list[1]
                    experience = str_list[2]
                elif len(str_list) > 1:
                    edu_v = str_list[1]

            # 公司
            company = div.xpath('./aside/text()').extract()[0]
            # print(company)

            print(title + " | " + pay + " | " + place + " | " + experience + " | " + edu_v + " | " + company)
            # break
            # # 职位招聘人数
            # count = div.xpath('')

