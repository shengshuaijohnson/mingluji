# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
import re
import urllib
import json
from scrapy.spiders import Spider
from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from minglu.items import Company
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MinglujiSpider(Spider):
    name = "mingluji"
    allowed_domains = ["mingluji.com"]
    start_urls = (
        'http://mingluji.com/node/7',
    )

    def parse(self, response):
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.101 Chrome/45.0.2454.101 Safari/537.36'}

        url_by_province = response.xpath(
            '//td[@class="views-field views-field-field-province"]//@href')

        for url in url_by_province:

            #list_url = url.extract() + "/list?page=1"
            list_url='http://gongshang.mingluji.com/shanghai/list?page=2'
            yield scrapy.Request(list_url,
                                 callback=self.parse_step2,
                                 headers=user_agent
                                 )
            break
        pass

    def pass_item(self,i):
        return i

    def parse_step2(self, response):
        print 111111111111
        print response.url

        try:
            max_page_content = response.xpath(
            '//li[@class="pager-last last"]//@href').extract()[0]
        except:
            return
        front_url, tmp = response.url.rsplit('=', 1)
        tmp, max_page_num = max_page_content.rsplit('=', 1)
        
        for i in range(1,int(max_page_num)+1):
            url = front_url + '={}'.format(i)
            yield scrapy.Request(url,
                             callback=self.parse_step3,
                             )


        pass

    def parse_step3(self, response):
        print "3333"
        
        province = re.search('com/(.*?)/', response.url).group(1)
        titles = response.xpath(
            '//div[@class="views-field views-field-title"]/span/a/text()')

        for title in titles:
            item = Company()
            item['name'] = title.extract()
            item['province'] = province
            yield self.pass_item(item)
        return
