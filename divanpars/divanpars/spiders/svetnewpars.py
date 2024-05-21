# Попробуй написать spider для нахождения всех источников
# освещения с сайта divan.ru
# Нужно взять название источника освещения, цену и ссылку

import scrapy

class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css("div._UdOk")
        for svet in svets:
            yield {
                "name": svet.css("div.lsooF span::text").get(),
                "price": svet.css("div.pY3d2 span::text").get(),
                "url": svet.css("a").attrib["href"]
            }

