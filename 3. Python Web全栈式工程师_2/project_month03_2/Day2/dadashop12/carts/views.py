import json

from django.http import JsonResponse
from django.views import View

from goods.models import SKU
from tools.login_decorator import login_check


# Create your views here.
class CartsView(View):
    @login_check
    def get(self, request, username):
        return JsonResponse({'code': 200})

    @login_check
    def post(self, request, username):
        json_str = request.body
        json_obj = json.loads(json_str)
        sku_id = json_obj['sku_id']
        count = json_obj['count']

        # 检查sku合法性
        try:
            sku = SKU.objects.get(id=sku_id, is_launched=True)
        except Exception as e:
            print(e)
            return JsonResponse({'code': 10400, 'error': 'SKU_id is invalid.'})

        count = int(count)
        if count > sku.stock:
            return JsonResponse({'code': 10401, 'error': 'Too many items'})

        return JsonResponse({'code': 200})
