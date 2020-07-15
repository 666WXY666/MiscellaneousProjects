import scrapy
import re
from q18_scrapy.q18_scrapy.items import Q18ScrapyItem


class mySpider(scrapy.spiders.Spider):
    name = "xuetang"
    allowed_domains = ["www.xuetangx.com/"]

    start_urls = ["http://www.xuetangx.com/partners"]

    def parse(self, response):
        item = Q18ScrapyItem()
        for each in response.xpath("/html/body/article[1]/section/ul/*"):
            item['school'] = each.xpath("a/div[2]/h3/text()").extract()
            item['num'] = each.xpath("a/div[2]/p[1]/text()").extract()
            if item['num']:
                item['num'] = re.findall(r'\d+', item['num'][0])
            if item['school'] and item['num']:
                yield (item)
    # def parse(self, response):
    #     item = Q18ScrapyItem()
    #     for i in range(1, 32):
    #         item['school'] = response.xpath \
    #             ("/html/body/article[1]/section/ul/li[{}]/a/div[2]/h3/text()".format(i)).extract()
    #         item['num'] = response.xpath \
    #             ("/html/body/article[1]/section/ul/li[{}]/a/div[2]/p[1]/text()".format(i)).extract()
    #         if item['school'] and item['num']:
    #             yield (item)
