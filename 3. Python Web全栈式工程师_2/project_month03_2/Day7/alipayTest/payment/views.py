import json

from alipay import AliPay
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
app_private_key_string = open(settings.ALIPAY_KEY_DIRS + 'app_private_key.pem').read()
alipay_public_key_string = open(settings.ALIPAY_KEY_DIRS + 'alipay_public_key.pem').read()

ORDER_STATUS = 1


class MyAliPay(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alipay = AliPay(
            appid=settings.ALIPAY_APP_ID,
            app_notify_url=None,
            app_private_key_string=app_private_key_string,
            alipay_public_key_string=alipay_public_key_string,
            sign_type='RSA2',
            debug=True
        )

    def get_trade_url(self, order_id, amount):
        order_string = self.alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,
            total_amount=amount,
            subject=order_id,
            return_url=settings.ALIPAY_RETURN_URL,
            notify_url=settings.ALIPAY_NOTIFY_URL
        )

        return 'https://openapi.alipaydev.com/gateway.do?' + order_string

    def get_verify_result(self, data, sign):
        return self.alipay.verify(data, sign)

    def get_trade_result(self, order_id):
        result = self.alipay.api_alipay_trade_query(out_trade_no=order_id)
        print(result)
        if result.get('trade_status') == 'TRADE_SUCCESS':
            return True
        return False


class OrderInfoView(MyAliPay):
    def get(self, request):
        return render(request, 'alipay.html')

    def post(self, request):
        json_obj = json.loads(request.body)
        order_id = json_obj.get('order_id')
        pay_url = self.get_trade_url(order_id, 10000)
        return JsonResponse({'code': 200, 'pay_url': pay_url})


class ResultView(MyAliPay):
    def get(self, request):
        print(request.GET)
        request_data = {k: request.GET[k] for k in request.GET.keys()}
        sign = request_data.pop('sign')
        is_verify = self.get_verify_result(request_data, sign)
        if is_verify:
            order_id = request_data.get('out_trade_no')
            if ORDER_STATUS == 2:
                return HttpResponse('支付成功')
            else:
                res = self.get_trade_result(order_id)
                if res:
                    # 更改订单状态
                    return HttpResponse('主动查询支付成功')
                else:
                    return HttpResponse('主动查询支付未成功')
        else:
            return HttpResponse('非法访问')

    def post(self, request):
        request_data = {k: request.POST[k] for k in request.POST.keys()}
        sign = request_data.pop('sign')
        is_verify = self.get_verify_result(request_data, sign)

        if is_verify:
            trade_status = request_data.get('trade_status')
            if trade_status == 'TRADE_SUCCESS':
                # 更改订单状态
                return HttpResponse('success')
            else:
                pass
        else:
            return HttpResponse('非法访问')
