import json

from django.shortcuts import render
from django.views import View


# Create your views here.
class OrderInfoView(View):
    def get(self, request):
        return render(request, 'alipay.html')

    def post(self, request):
        json_obj = json.loads(request.body)
        order_id = json_obj.get('order_id')
