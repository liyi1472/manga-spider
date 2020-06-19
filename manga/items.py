import scrapy


class MangaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book = scrapy.Field()
    page = scrapy.Field()
    src = scrapy.Field()
