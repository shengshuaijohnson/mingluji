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
import requests
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

count = 0


class WhySpider(Spider):
    name = 'why'
    start_urls = (
        'http://www.chazidian.com/kepu-1/',
    )

    def parse(self, response):
        template = 'http://www.chazidian.com/kepu-1/{}/'
        for i in range(1, 64):
            url = template.format(i)
            print url
            yield scrapy.Request(url, callback=self.parse2)

    def return_item(self, i):
        return i

    def parse2(self, response):
        tmp = response.xpath('//div[@class="box_content"]//li//@href')
        items = []
        for i in tmp:
            url = i.extract()
            res = requests.get(url)
            content = res.text
            title = re.search(
                '<span id="print_title">(.*?)</span>', content).group(1)
            answer = re.search(
                '<div id="print_content">([\s\S]*?)(</div|<span|<meta|<BR|<pstyle)', content)
            index = hashlib.md5(title).hexdigest()
            if not answer:
            	    print "1111111111111"
            	    print url
            	    continue
            answer = re.sub('<p>|</p>', '', answer.group(1))
            answer = re.sub('\r|\n|\t', '', answer)
            answer = re.sub('&([a-zA-Z0-9]+?);', '', answer)
            answer =re.sub('<p([\s\S]?)>','',answer)
            answer=answer.replace(u'<br>',u'')
            answer=answer.replace(u'<br >',u'')
            item = Company()
            item['question'] = title
            item['answers'] = answer
            item['id'] = index
            items.append(item)

        for i in items:
            yield self.return_item(i)

