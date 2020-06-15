import scrapy
from scrapy_splash import SplashRequest
from manga.items import MangaItem


class FzdmSpider(scrapy.Spider):
    name = 'fzdm'
    allowed_domains = ['manhua.fzdm.com']

    def start_requests(self):
        # 153《鬼灭之刃》1-205话完结
        manga_base = 'http://manhua.fzdm.com/153/'
        # for i in range(1, 1 + 205):
        for i in range(1, 1 + 1):
            yield SplashRequest(manga_base + str(i), self.parse, args={'wait': 5})
    
    def parse(self, response):
        src = response.css("#mhpic::attr('src')").get()
        item = MangaItem()
        item['image_urls'] = [src]
        yield item
