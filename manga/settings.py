BOT_NAME = 'manga'
SPIDER_MODULES = ['manga.spiders']
NEWSPIDER_MODULE = 'manga.spiders'
CONCURRENT_REQUESTS = 1000
IMAGES_STORE = 'images'
RETRY_TIMES = 10000
ITEM_PIPELINES = {
    'manga.pipelines.MangaPipeline': 300,
}