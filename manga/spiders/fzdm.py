import scrapy
from scrapy_splash import SplashRequest
from manga.items import MangaItem


class FzdmSpider(scrapy.Spider):
    name = 'fzdm'
    allowed_domains = ['manhua.fzdm.com']

    def start_requests(self):
        # 153《鬼灭之刃》1-205话完结
        base = 'http://manhua.fzdm.com/153/'
        yield SplashRequest(base, self.parseBook, args={'wait': 5})
        
    def parseBook(self, response):
        urls = response.css('#content li a::attr("href")').getall()
        books = response.css('#content li a::text').getall()
        for i, url in enumerate(urls):
            request = SplashRequest(response.url + str(url), self.parsePage, args={'wait': 5})
            request.meta['url'] = response.url + str(url)
            request.meta['book'] = books[i]
            yield request

    def parsePage(self, response):
        item = MangaItem()
        item['image_urls'] = response.css("#mhpic::attr('src')").getall()
        item['page'] = response.css(".navigation .button-success::text").getall()
        yield item
        if '下一页' == response.css('.navigation .pure-button.pure-button-primary::text').getall()[-1]:
            next_url = response.css('.navigation .pure-button.pure-button-primary::attr("href")').getall()[-1]
            request = SplashRequest(response.meta['url'] + next_url, self.parsePage, args={'wait': 5})
            request.meta['url'] = response.meta['url']
            request.meta['book'] = response.meta['book']
            yield request