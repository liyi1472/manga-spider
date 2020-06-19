BOT_NAME = 'manga'
SPIDER_MODULES = ['manga.spiders']
NEWSPIDER_MODULE = 'manga.spiders'
CONCURRENT_REQUESTS = 5000
RETRY_TIMES = 10000

SPLASH_URL = 'http://localhost:8050'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

ITEM_PIPELINES = {
    'manga.pipelines.MangaPipeline': 300,
}
IMAGES_STORE = 'images'
