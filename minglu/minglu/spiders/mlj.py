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
        print response
        url_by_province = response.xpath(
            '//td[@class="views-field views-field-field-province"]//@href')
        for url in url_by_province:
            list_url = url.extract() + "/list?page=1"
            yield scrapy.Request(list_url,
                                 callback=self.parse_step2,
                                 )
        pass

    def parse_step2(self, response):
        max_page_content=response.xpath('//li[@class="pager-last last"]//@href')
        front_url,tmp=response.url.rsplit('=',1)
        for i in max_page_content:
        	tmp,max_page=i.extract().rsplit('=',1)
        	for index in range(max_page+1)
	url=front_url+'='+index
	self.parse_page(url)

        	#print max_page_num

        pass

    def parse_page(self, url):
        item=Company()
        
        pass
