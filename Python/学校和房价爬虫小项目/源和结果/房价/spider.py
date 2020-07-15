import scrapy
import re
from q19_scrapy.q19_scrapy.items import Q19ScrapyItem


class mySpider(scrapy.spiders.Spider):
    name = "loufang"
    allowed_domains = ["www.bj.fang.lianjia.com/"]
    start_urls = []
    for page in range(1, 5):
        url = "https://bj.fang.lianjia.com/loupan/nhs1pg{}/".format(page)
        start_urls.append(url)

        def parse(self, response):
            item = Q19ScrapyItem()
            for each in response.xpath("/html/body/div[4]/ul[2]/*"):
                item['name'] = each.xpath("div/div[1]/a/text()").extract()
                item['price'] = each.xpath("div/div[6]/div[1]/span[1]/text()").extract()
                item['unit'] = each.xpath("div/div[6]/div[1]/span[2]/text()").extract()
                item['size'] = each.xpath("div/div[3]/span/text()").extract()
                if item['unit']:
                    item['unit'][0] = item['unit'][0].replace(u'\xa0', u'')
                if item['size']:
                    item['size'] = re.findall(r'\d+', item['size'][0])
                if item['name'] and item['price'] and item['size']:
                    yield (item)
