# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

import urllib
import json
from scrapy.spiders import Spider
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MinglujiSpider(Spider):
    name = "mingluji"
    allowed_domains = ["mingluji.com"]
    start_urls = (
        'http://mingluji.com/node/7',
    )

    def parse(self,response):
    	print 'parse'
    	return
