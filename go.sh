docker stop splash
docker run --rm -d --name splash -p 8050:8050 scrapinghub/splash
scrapy crawl fzdm