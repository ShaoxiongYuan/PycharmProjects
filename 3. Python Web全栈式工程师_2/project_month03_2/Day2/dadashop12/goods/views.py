import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View
from django.conf import settings

from tools.cache_decorator import cache_check
from .models import *


# Create your views here.
class GoodsIndexView(View):
    def get(self, request):
        print('index view in')

        all_cata = Catalog.objects.all()
        res = []

        for cata in all_cata:
            cata_dict = {'catalog_id': cata.id, 'catalog_name': cata.name}
            # 获取该品类下所有spu的id
            spu_ids = SPU.objects.filter(catalog=cata.id).values('id')
            sku_list = SKU.objects.filter(spu__in=spu_ids, is_launched=True)[:3]
            cata_dict['sku'] = []
            for sku in sku_list:
                sku_dict = {
                    'skuid': sku.id,
                    'name': sku.name,
                    'caption': sku.caption,
                    'price': str(sku.price),
                    'image': str(sku.default_image_url)
                }
                cata_dict['sku'].append(sku_dict)
            res.append(cata_dict)

        result = {'code': 200, 'data': res, 'base_url': settings.PIC_URL}
        return JsonResponse(result)


class GoodsListView(View):
    def get(self, request, catalog_id):
        """
        获取列表页内容
        :param request:
        :param catalog_id: 分类id
        :param page_num: 第几页
        :param page_size: 每页显示多少项
        :return:
        """
        # 127.0.0.1:8000/v1/goods/catalogs/1/?launched=true&page=1
        # 0. 获取url传递参数值
        launched = bool(request.GET.get('launched', True))
        page_num = request.GET.get('page', 1)
        # 1.获取分类下的sku列表
        spu_list_ids = SPU.objects.filter(catalog=catalog_id).values("id")
        sku_list = SKU.objects.filter(spu__in=spu_list_ids, is_launched=launched).order_by("id")
        # 2.分页
        # 创建分页对象，指定列表、页大小
        page_num = int(page_num)
        page_size = 9
        try:
            paginator = Paginator(sku_list, page_size)
            # 获取指定页码的数据
            page_skus = paginator.page(page_num)
            page_skus_json = []
            for sku in page_skus:
                sku_dict = dict()
                sku_dict['skuid'] = sku.id
                sku_dict['name'] = sku.name
                sku_dict['price'] = str(sku.price)
                sku_dict['image'] = str(sku.default_image_url)
                page_skus_json.append(sku_dict)
        except:
            result = {'code': 40200, 'error': '页数有误，小于0或者大于总页数'}
            return JsonResponse(result)
        result = {'code': 200, 'data': page_skus_json, 'paginator': {'pagesize': page_size, 'total': len(sku_list)},
                  'base_url': settings.PIC_URL}
        return JsonResponse(result)


class GoodsDetailView(View):
    @cache_check(key_prefix='gd', key_param='sku_id', cache='goods_detail')
    def get(self, request, sku_id):
        """
        获取sku详情页信息，获取图片暂未完成
        :param request:
        :param sku_id: sku的id
        :return:
        """
        # 127.0.0.1:8000/v1/goods/detail/1
        # 获取sku实例
        print('----goods detail view in----')

        sku_details = {}

        try:
            sku_item = SKU.objects.get(id=sku_id)
        except Exception as e:
            print(e)
            # 判断是否有当前sku
            result = {'code': 40300, 'error': "Such sku doesn't exist"}
            return JsonResponse(result)
        sku_catalog = sku_item.spu.catalog
        sku_details['image'] = str(sku_item.default_image_url)
        sku_details["spu"] = sku_item.spu.id
        sku_details["name"] = sku_item.name
        sku_details["caption"] = sku_item.caption
        sku_details["price"] = str(sku_item.price)
        sku_details["catalog_id"] = sku_catalog.id
        sku_details["catalog_name"] = sku_catalog.name

        # 详情图片
        sku_image = SKUImage.objects.filter(sku=sku_item)
        if sku_image:
            sku_details['detail_image'] = str(sku_image[0].image)
        else:
            sku_details['detail_image'] = ""

        sku_sale_attr_id = []  # 存放销售属性id
        sku_sale_attr_names = []  # 存放销售属性name
        spu_sale_attrs = SPUSaleAttr.objects.filter(spu=sku_item.spu.id)
        for attr in spu_sale_attrs:
            sku_sale_attr_id.append(attr.id)
            sku_sale_attr_names.append(attr.name)

        sku_sale_attr_val_id = [i.id for i in sku_item.sale_attr_value.all()]

        # TODO
        sku_all_sale_attr_vals_id = {}
        sku_all_sale_attr_vals_name = {}
        for id in sku_sale_attr_id:
            items = SaleAttrValue.objects.filter(spu_sale_attr=id)
            sku_all_sale_attr_vals_id[id] = []
            sku_all_sale_attr_vals_name[id] = []
            for item in items:
                sku_all_sale_attr_vals_id[id].append(item.id)
                sku_all_sale_attr_vals_name[id].append(item.name)

        sku_details['sku_sale_attr_id'] = sku_sale_attr_id
        sku_details['sku_sale_attr_names'] = sku_sale_attr_names
        sku_details['sku_sale_attr_val_id'] = sku_sale_attr_val_id
        sku_details['sku_all_sale_attr_vals_id'] = sku_all_sale_attr_vals_id
        sku_details['sku_all_sale_attr_vals_name'] = sku_all_sale_attr_vals_name

        # sku规格部分
        # 用于存放规格相关数据，格式：{规格名称1: 规格值1, 规格名称2: 规格值2, ...}
        spec = dict()
        sku_spec_values = SKUSpecValue.objects.filter(sku=sku_id)
        if not sku_spec_values:
            sku_details['spec'] = dict()
        else:
            for sku_spec_value in sku_spec_values:
                spec[sku_spec_value.spu_spec.name] = sku_spec_value.name
            sku_details['spec'] = spec

        result = {'code': 200, 'data': sku_details, 'base_url': settings.PIC_URL}
        return JsonResponse(result)


class GoodsChangeSkuView(View):
    def post(self, request):
        data = json.loads(request.body)
        # 将前端传来的销售属性值id放入列表
        sku_vals = []
        result = {}
        for k in data:
            if 'spuid' != k:
                sku_vals.append(data[k])
        sku_list = SKU.objects.filter(spu=data['spuid'])

        for sku in sku_list:
            sku_details = dict()
            sku_details['sku_id'] = sku.id
            # 获取sku销售属性值id

            sku_sale_attr_val_id = [i.id for i in sku.sale_attr_value.all()]

            if sku_vals == sku_sale_attr_val_id:
                result = {"code": 200, "data": sku.id, }
        if len(result) == 0:
            result = {"code": 40050, "error": "no such sku", }
        return JsonResponse(result)
