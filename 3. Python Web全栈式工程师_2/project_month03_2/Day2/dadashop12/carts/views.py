import json

from django.conf import settings
from django.core.cache import caches
from django.http import JsonResponse
from django.views import View

from goods.models import SKU
from tools.login_decorator import login_check

# Create your views here.
CARTS_CACHE = caches['carts']


class CartsView(View):
    def get_cache_key(self, uid):
        return 'carts_%s' % uid

    def get_carts_all_data(self, uid):
        key = self.get_cache_key(uid)
        data = CARTS_CACHE.get(key)
        if not data:
            return {}
        r_data = {int(k): v for k, v in data.items()}
        return r_data

    def set_carts_data(self, uid, sku_id, data):
        key = self.get_cache_key(uid)
        all_data = self.get_carts_all_data(uid)
        all_data[int(sku_id)] = data
        CARTS_CACHE.set(key, all_data)

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

        user = request.myuser
        carts = self.get_carts_all_data(user.id)

        if not carts:
            my_sku_info = [count, 1]
        else:
            my_sku_info = carts.get(sku.id)
            if not my_sku_info:
                my_sku_info = [count, 1]
            else:
                old_count = my_sku_info[0]
                new_count = count + old_count
                if new_count > sku.stock:
                    return JsonResponse({'code': 10402, 'error': 'Too many items'})
                my_sku_info = [new_count, 1]
        self.set_carts_data(user.id, sku.id, my_sku_info)

        carts_data = self.get_carts_all_data(user.id)
        sku_count = len(carts_data)

        return JsonResponse({'code': 200, 'data': {'carts_count': sku_count}, 'base_url': settings.PIC_URL})
