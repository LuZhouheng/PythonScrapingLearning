# -*- coding: utf-8 -*-
# @Author: LuZhouheng
# @Date:   2016-05-14 13:21:01

from scrapy.contrib.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class ArticleSpider(CrawlSpider):
    name="article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    rules = [Rule(SgmlLinkExtractor(allow=('(/wiki/)((?!:).)*$'),),callback="parse_item", follow=True)]

    def parse_item(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: "+title)
        item['title'] = title
        return item

#--------------------------------------------------------------------------------------------------------------------------------#
# Simple Article Spider
# -*- coding: utf-8 -*-
# @Author: LuZhouheng
# @Date:   2016-05-14 13:00:39
#这个爬虫先进入 start_urls 里面的两个页面，收集信息，然后停止。

# from scrapy.selector import Selector
# from scrapy import Spider
# from wikiSpider.items import Article

# class ArticleSpider(Spider):
#     name="article"
#     allowed_domains = ["en.wikipedia.org"]
#     start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
#         "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]

#     def parse(self, response):
#         item = Article()
#         title = response.xpath('//h1/text()')[0].extract()
#         print("Title is: " + title)
#         item['title'] = title
#         return item