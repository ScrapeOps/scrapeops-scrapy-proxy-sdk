ScrapeOps Proxy Middleware for Scrapy
=======================================================
The ScrapeOps Scrapy Proxy Middleware is an easy way to integrate the [ScrapeOps Proxy API](https://scrapeops.io/proxy-aggregator/) into your [Scrapy](https://scrapy.org/) spiders.

To use the middleware you first need to get a [free API key here](https://scrapeops.io/app/register/proxy) if you don't have one already.

Install Using Pip
--------
To install the ScrapeOps Scrapy Proxy Middleware simply use pip:


```
pip install scrapeops-scrapy-proxy-sdk
```   


Integrating Into Your Scrapy Project
-----------

Integrate into your Scrapy project by updating your ``settings.py`` file:

```python
SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

  
SCRAPEOPS_PROXY_ENABLED = True


DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

``` 

Now when you run your spiders, the requests will be automatically sent through the [ScrapeOps Proxy API](https://scrapeops.io/proxy-aggregator/).


Enabling Advanced Functionality
-----------
The ScrapeOps Proxy API supports a [range of more advanced features](https://scrapeops.io/docs/proxy-aggregator/advanced-functionality/functionality-list/) that you can enable by adding extra query parameters to your request.

To enable them using the ScrapeOps Scrapy Proxy Middleware you can do so using 3 methods:

### Method #1: Global Project Settings
You can apply the proxy setting to every spider that runs in your project by adding a ``SCRAPEOPS_PROXY_SETTINGS`` dictionary to your ``settings.py`` file with the extra features you want to enable.


```python

SCRAPEOPS_API_KEY = 'YOUR_API_KEY'
SCRAPEOPS_PROXY_ENABLED = True
SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}

DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

``` 

---

### Method #2: Spider Settings
You can apply the proxy setting to every request a spider makes by adding a ``SCRAPEOPS_PROXY_SETTINGS`` dictionary to the ``custom_settings`` attribute in your spider with the extra features you want to enable.

```python

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {
        'SCRAPEOPS_PROXY_SETTINGS': {'country': 'us'}
    }

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass

``` 

---

### Method #3: Request Settings
You can apply the proxy setting to each individual request a spider makes by adding the extra features you want to enable to the `meta` parameter of each request.

When using this method you need to add **'sops_'** to the start of the feature you key you want to enable. So to enable ``'country': 'uk'``, you would use `'sops_country': 'uk'`.

```python

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, meta={'sops_country': 'uk'}, callback=self.parse)

    def parse(self, response):
        pass

``` 

A full list of advanced features can be found [here](https://scrapeops.io/docs/proxy-aggregator/advanced-functionality/functionality-list/).

---

## Concurrency Management
When using Scrapy with the ScrapeOps Proxy you need to make sure you don't exceed your concurrency limit of the plan you are using.

For example, if you were using the **Free Plan** which has a concurrency limit of **1 thread**, then you would set `CONCURRENT_REQUESTS=1` in your `settings.py` file.

For maximum performance you would also ensure that `DOWNLOAD_DELAY` is set to zero in your `settings.py` file (this is the default setting).

```python
## settings.py

CONCURRENT_REQUESTS=1
DOWNLOAD_DELAY=0

```