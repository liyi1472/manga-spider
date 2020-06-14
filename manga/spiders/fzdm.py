import scrapy
from ..items import MangaItem


class FzdmSpider(scrapy.Spider):
    name = 'fzdm'
    allowed_domains = ['manhua.fzdm.com']
    start_urls = []
    # 153《鬼灭之刃》1-205话完结
    manga_base = 'http://manhua.fzdm.com/153/'
    # for i in range(1, 1 + 205):
    for i in range(1, 1 + 1):
        start_urls.append(manga_base + str(i))

    def parse(self, response):
        src = response.css("#mhpic::attr('src')").get()
        item = MangaItem()
        item['src'] = [src]
        yield item
