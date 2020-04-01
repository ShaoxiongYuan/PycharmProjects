from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法 process_response 被调用")
        return response


class MyMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法 process_request2 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view2 被调用")

    def process_response(self, request, response):
        print("中间件方法 process_response2 被调用")
        return response


class MyMiddleware3(MiddlewareMixin):
    visit_time = {}

    def process_request(self, request):
        ip_addr = request.META['REMOTE_ADDR']
        path_info = request.path_info
        if path_info != '/middleware':
            return
        times = self.visit_time.get(ip_addr, 0)
        self.visit_time[ip_addr] = times + 1
        if times < 5:
            return
        return HttpResponse('Sorry')
