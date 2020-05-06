# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals
from .proxypool import proxy_list


class MiddleSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MiddleDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


from fake_useragent import UserAgent


class MiddleRandomUADownloaderMiddleware:
    def process_request(self, request, spider):
        """
        随机UA
        :param request:
        :param spider:
        :return:
        """
        agent = UserAgent().random
        request.headers['User-Agent'] = agent
        print(agent)


class MiddleRandomProxyDownloaderMiddleware:
    def process_request(self, request, spider):
        proxy = random.choice(proxy_list)
        request.meta['proxy'] = proxy
        print(proxy)

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        return request


class MiddleCookieDownloaderMiddleware:
    def process_request(self, request, spider):
        cookies = self.get_cookies()
        request.cookies = cookies

    def get_cookies(self):
        cook_str = 'BIDUPSID=A28F01A47DBE44F0B5F5238F07800683; PSTM=1588650485; BAIDUID=A28F01A47DBE44F06DFEB24DEB031B36:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=0_0_1_0_0_1_0_0_0_1_0_0_0_0_0_0_0_0_1588651943%7C1%230_0_1588651943%7C1; BDUSS=p2TkgwdE5kaDUyN0t4d3JMUjFoVnZUbjJyMlVINExDb3JoRVVISn5rcUV-TmhlRVFBQUFBJCQAAAAAAAAAAAEAAAAqmQ9p1KzJ3NDbysfO0gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIRvsV6Eb7FeQ0; cflag=13%3A3; BD_HOME=1; H_PS_PSSID=1423_31326_21127_31423_31341_31270_31464_31228_30823_31164; sugstore=1'

        cookies = {}
        for kv in cook_str.split('; '):
            key = kv.split('=')[0]
            value = kv.split('=')[1]
            cookies[key] = value
        return cookies
