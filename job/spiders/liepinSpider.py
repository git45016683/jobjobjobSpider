'''
Author: your name
Date: 2021-04-25 11:40:59
LastEditTime: 2021-04-25 16:36:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \job\job\spiders\liepinSpider.py
'''
import scrapy
from job.items import JobItem


class LiepinspiderSpider(scrapy.Spider):
    name = 'liepinSpider'
    allowed_domains = ['www.liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?flushckid=1&compkind=&dqs=050020&pubTime=&pageSize=40&salary=20%2450&compTag=&sortFlag=15&compIds=&subIndustry=&industryType=industry_02&jobKind=&industries=050&compscale=&key=%E6%8A%80%E6%9C%AF%E7%AE%A1%E7%90%86&siTag=G-I_JtdsLVjIcDtYV31HIw%7EnBIcYTf8hlCPB-Kl8hs1Zw&d_sfrom=search_fp&d_ckId=6a9549e52f5598efa031eb0bd7ccfa77&d_curPage=0&d_pageSize=40&d_headId=cae87a9ba362c94c1fc09f6725e7094a']
    # start_urls = ['https://www.liepin.com/a/25713837.shtml']

    def parse(self, response):
        # print(response)
        domain = 'www.liepin.com'
        job_list = response.xpath('//*[@class="sojob-result "]/ul/li')
        # print(job_list)
        for li in job_list:
            # print(li)
            
            jobItem = JobItem()
            title = ""
            pay = ""
            place = ""
            edu_v = ''
            experience = ''
            company = ""
            url = ""
            
            # 职位名称
            title = li.xpath('./div/div[1]/h3/a/text()').extract()[0].strip()
            # print(title)
            
            # 职位待遇
            pay = li.xpath('./div/div[1]/p/span[1]/text()').extract()[0]
            # print(pay)

            # 职位工作地点
            place = li.xpath('./div/div[1]/p/a/text()').extract()[0]
            # print(place)

            # 工作学历要求
            edu_v = li.xpath('./div/div[1]/p/span[2]/text()').extract()[0]
            # print(edu_v)
            
            # 工作经验要求
            experience = li.xpath('./div/div[1]/p/span[3]/text()').extract()[0]
            # print(experience)

            # 公司
            company = li.xpath('./div/div[2]/p[1]/a/text()').extract()[0]
            # print(company)

            # # 详情链接-参数
            # data_pro = li.xpath('./div/div[1]/h3/a/@data-promid').extract()[0]
            # print(data_pro)

            # 详情链接
            detail_url = li.xpath('./div/div[1]/h3/a/@href').extract()[0]
            # print(detail_url)
            if(detail_url.startswith('/')):
                detail_url = domain + detail_url
                if('://' not in detail_url):
                    detail_url = 'https://' + detail_url
            url = detail_url
            # print(title + " | " + pay + " | " + place + " | " + experience + " | " + edu_v + " | " + company + " | " + url)
            
            jobItem['title'] = title
            jobItem['pay'] = pay
            jobItem['place'] = place
            jobItem['experience'] = experience
            jobItem['edu_v'] = edu_v
            jobItem['company'] = company
            jobItem['url'] = url
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={"item":jobItem})


    def parse_detail(self, response):
        item = response.meta['item']
        # print(response.url)
        if ('/a' in response.url):
            job_info = response.xpath('//*[@class="job-main job-description main-message"]/div[1]//text()').extract()
        else:
        # job_info = response.xpath('//*[@class="content content-word"]//text()').extract()
            job_info = response.xpath('//*[@class="job-item main-message job-description"]/div[1]//text()').extract()
        job_info = ''.join(job_info).strip()
        job_info = job_info
        item['job_info'] = job_info
        # print(item)
        print('------------------------------------------------------------------------------------')
        yield item

