from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request


class MangaPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['src'], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        path = item['book'] + '/' + item['page']
        return '%s.jpg' % (path)