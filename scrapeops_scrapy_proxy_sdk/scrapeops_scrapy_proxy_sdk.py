from urllib.parse import urlencode, urlparse, parse_qs
from scrapy import Request

class ScrapeOpsScrapyProxySdk(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):
        self.scrapeops_proxy_settings = {}
        self.scrapeops_api_key = settings.get('SCRAPEOPS_API_KEY')
        self.scrapeops_endpoint = 'https://proxy.scrapeops.io/v1/?'
        self.scrapeops_proxy_active = settings.get('SCRAPEOPS_PROXY_ENABLED', False)
        self._clean_proxy_settings(settings.get('SCRAPEOPS_PROXY_SETTINGS'))

    def _clean_proxy_settings(self, proxy_settings):
        if proxy_settings is not None:
            for key, value in proxy_settings.items():
                clean_key = key.replace('sops_', '')
                self.scrapeops_proxy_settings[clean_key] = value

    @staticmethod
    def _get_requested_url(url):
        parsed_url = urlparse(url)
        raw_url = parse_qs(parsed_url.query).get('url', url)
        if isinstance(raw_url, str) or isinstance(raw_url, bytes):
            return raw_url
        elif isinstance(raw_url, list):
            return ''.join([str(elem) for elem in raw_url])

    @staticmethod
    def _replace_response_url(response):
        real_url = response.headers.get(
            'Sops-Final-Url', def_val=ScrapeOpsScrapyProxySdk._get_requested_url(response.url))
        return response.replace(
            url=real_url.decode(response.headers.encoding))
    
    def _get_scrapeops_url(self, request):
        payload = {'api_key': self.scrapeops_api_key, 'url': request.url}

        ## Global Request Settings
        if self.scrapeops_proxy_settings is not None:
            for key, value in self.scrapeops_proxy_settings.items():
                payload[key] = value

        ## Request Level Settings 
        for key, value in request.meta.items():
            if 'sops_' in key:
                clean_key = key.replace('sops_', '')
                payload[clean_key] = value

        proxy_url = self.scrapeops_endpoint + urlencode(payload)
        return proxy_url

    def _scrapeops_proxy_enabled(self):
        if self.scrapeops_api_key is None or self.scrapeops_api_key == '' or self.scrapeops_proxy_active == False:
            return False
        return True
    
    def process_request(self, request, spider):
        if self._scrapeops_proxy_enabled is False or self.scrapeops_endpoint in request.url:
            return None
        
        scrapeops_url = self._get_scrapeops_url(request)
        new_request = request.replace(
            cls=Request, url=scrapeops_url, meta=request.meta)
        return new_request

    def process_response(self, request, response, spider):
        new_response = self._replace_response_url(response)
        return new_response