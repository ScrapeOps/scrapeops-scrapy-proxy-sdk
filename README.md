ScrapeOps middleware for Scrapy (http://scrapy.org/)
=======================================================

Processes Scrapy requests using ScapeOps


Install with pip
--------


    pip install scrapeops-scrapy-proxy-sdk



Add to your scrapy project settings.py file
-----------


    SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

  
    SCRAPEOPS_PROXY_ENABLED = True


    DOWNLOADER_MIDDLEWARES = {
        'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    }