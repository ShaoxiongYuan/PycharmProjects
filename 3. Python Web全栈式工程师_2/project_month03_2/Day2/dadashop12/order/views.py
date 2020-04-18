import datetime
import json

from django.conf import settings
from django.db import transaction
from django.http import JsonResponse
from django.views import View

from carts.views import CartsView
from .models import *
from tools.login_decorator import login_check
from user.models import Address
from goods.models import SKU


# Create your views here.
class AdvanceOrderView(View):
    @login_check
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_address(self, uid):
        all_address = Address.objects.filter(user_profile=uid, is_active=True)

        address_default = []
        address_no_default = []
        for addr in all_address:
            addr_dict = {
                'id': addr.id,
                'name': addr.receiver,
                'mobile': addr.receiver_mobile,
                'title': addr.tag,
                'address': addr.address
            }
            if addr.is_default:
                address_default.append(addr_dict)
            else:
                address_no_default.append(addr_dict)

        return address_default + address_no_default

    def get_carts_order_list(self, uid):
        cart_obj = CartsView()
        sku_list = cart_obj.get_carts_list(uid)
        return [s for s in sku_list if s['selected'] == 1]

    def get(self, request, username):
        user = request.myuser
        address_list = self.get_address(user.id)
        settlement = int(request.GET.get('settlement_type'))

        if settlement:
            sku_list = []
        else:
            sku_list = self.get_carts_order_list(user.id)
            if not sku_list:
                return JsonResponse({'code': 10500, 'error': 'No items in cart.'})

        data = {
            'addresses': address_list,
            'sku_list': sku_list
        }
        return JsonResponse({'code': 200, 'data': data, 'base_url': settings.PIC_URL})


class OrderInfoView(View):
    @login_check
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_carts_order_data(self, uid):
        carts_obj = CartsView()
        all_data = carts_obj.get_carts_all_data(uid)
        return {k: v for k, v in all_data.items() if v[1] == 1}

    def del_carts_order_data(self, uid, sku_ids):
        carts_obj = CartsView()
        for sku_id in sku_ids:
            carts_obj.del_carts_data(uid, sku_id)

    def post(self, request, username):
        user = request.myuser
        json_str = request.body
        json_obj = json.loads(json_str)
        address_id = json_obj.get('address_id')

        # 校验地址
        try:
            address = Address.objects.get(user_profile=user.id, id=address_id)
        except Exception as e:
            print(e)
            return JsonResponse({'code': 10501, 'errmsg': 'Address is wrong.'})

        with transaction.atomic():
            sid = transaction.savepoint()
            now = datetime.datetime.now()
            order_id = '%s%02d' % (now.strftime('%Y%m%d%H%M%S'), user.id)
            total_count = 0
            total_amount = 0
            order = OrderInfo.objects.create(
                order_id=order_id,
                user_id=user.id,
                address=address.address,
                receiver=address.receiver,
                receiver_mobile=address.receiver_mobile,
                tag=address.tag,
                total_amount=total_amount,
                total_count=total_count,
                freight=1,
                pay_method=1,
                status=1
            )
            carts_dict = self.get_carts_order_data(user.id)
            skus = SKU.objects.filter(id__in=carts_dict.keys())

            for sku in skus:
                if not sku.is_launched:
                    continue
                carts_count = carts_dict[sku.id][0]
                if carts_count > sku.stock:
                    transaction.savepoint_rollback(sid)
                    return JsonResponse({'code': 10502, 'errmsg': 'The commodity [%s] is out of stock.' % sku.name})

                old_version = sku.version
                result = SKU.objects.filter(
                    id=sku.id,
                    version=old_version
                ).update(
                    stock=sku.stock - carts_count,
                    sales=sku.sales + carts_count,
                    version=old_version + 1
                )

                # 有人修改库存量
                if result == 0:
                    transaction.savepoint_rollback(sid)
                    return JsonResponse({'code': 10503, 'errmsg': '服务器正忙，请稍后重试！'})

                OrderGoods.objects.create(
                    order_info_id=order_id,
                    sku_id=sku.id,
                    count=carts_count,
                    price=sku.price
                )

                total_count += carts_count
                total_amount += sku.price * carts_count

            # 修改订单数据总金额，总数量
            order.total_amount = total_amount
            order.total_count = total_count
            order.save()

            transaction.savepoint_commit(sid)

        # 购物车选中数据清除
        self.del_carts_order_data(user.id, carts_dict.keys())

        data = {
            'saller': '达达商城',
            'total_amount': order.total_amount + order.freight,
            'order_freight': order.freight,
            'order_id': order_id,
            'pay_url': ''
        }
        return JsonResponse({'code': 200, 'data': data})
