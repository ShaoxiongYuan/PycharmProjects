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
    @login_check
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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

    def get_carts_list(self, uid):
        # [{"id":"","name":"","count":"","selected":"","default_image_url":"","price":"","sku_sale_attr_name":[],"sku_sale_attr_val":[]},{"":""...}]
        carts_data = self.get_carts_all_data(uid)
        if not carts_data:
            return []

        skus_list = []
        skus = SKU.objects.filter(id__in=carts_data.keys())
        for sku in skus:
            sku_dict = {
                'id': sku.id,
                'name': sku.name,
                'count': carts_data[sku.id][0],
                'selected': carts_data[sku.id][1],
                'default_image_url': str(sku.default_image_url),
                'price': str(sku.price)
            }

            sku_sale_attr_name = []
            sku_sale_attr_value = []
            sale_attr_values = sku.sale_attr_value.all()
            for attr_value in sale_attr_values:
                sku_sale_attr_value.append(attr_value.name)
                sku_sale_attr_name.append(attr_value.spu_sale_attr.name)
            sku_dict['sku_sale_attr_name'] = sku_sale_attr_name
            sku_dict['sku_sale_attr_val'] = sku_sale_attr_value

            skus_list.append(sku_dict)
        return skus_list

    def merge_carts(self, uid, carts_info):
        carts_data = self.get_carts_all_data(uid)
        if not carts_info:
            # 离线状态未使用购物车
            return len(carts_data)

        for c_dic in carts_info:
            sku_id = int(c_dic['id'])
            try:
                sku_data = SKU.objects.get(id=sku_id, is_launched=True)
            except Exception as e:
                print(e)
                continue

            c_count = int(c_dic['count'])
            if sku_id in carts_data:
                sku_count = int(carts_data[sku_id][0])
                final_count = min(max(c_count, sku_count), int(sku_data.stock))
                carts_data[sku_id][0] = final_count
            else:
                carts_data[sku_id] = [min(sku_data.stock, c_count), 1]

            self.set_carts_data(uid, sku_id, carts_data[sku_id])
            return len(carts_data)

    def del_carts_data(self, uid, sku_id):
        key = self.get_cache_key(uid)
        carts_data = self.get_carts_all_data(uid)
        if sku_id in carts_data:
            del carts_data[sku_id]
            CARTS_CACHE.set(key, carts_data)

    def get(self, request, username):
        skus_list = self.get_carts_list(request.myuser.id)
        return JsonResponse({'code': 200, 'data': skus_list, 'base_url': settings.PIC_URL})

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

    def put(self, request, username):
        pass

    def delete(self, request, username):
        pass
