from scrapy import Spider
from scrapy import Request
from manga.items import MangaItem
import re


class FzdmSpider(Spider):
    name = 'fzdm'

    def start_requests(self):
        # 鬼灭之刃:153
        # 海贼王:2
        base = 'http://manhua.fzdm.com/2/'
        yield Request(base, self.parseBook)
        
    def parseBook(self, response):
        books = response.css('#content li a::text').getall()
        urls = response.css('#content li a::attr("href")').getall()
        for i, url in enumerate(urls):
            request = Request(response.url + str(url), self.parsePage)
            request.meta['book'] = books[i]
            request.meta['url'] = response.url + str(url)
            yield request

    def parsePage(self, response):
        item = MangaItem()
        item['book'] = response.meta['book']
        item['page'] = response.css(".navigation .button-success::text").get()
        item['src'] = 'http://p17.manhuapan.com/' + response.css('script').re(r'mhurl="(.*?)"')[0]
        yield item
        if '下一页' == response.css('.navigation .pure-button.pure-button-primary::text').getall()[-1]:
            next_url = response.css('.navigation .pure-button.pure-button-primary::attr("href")').getall()[-1]
            request = Request(response.meta['url'] + next_url, self.parsePage)
            request.meta['book'] = response.meta['book']
            request.meta['url'] = response.meta['url']
            yield request