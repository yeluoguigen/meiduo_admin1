from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import SKU, GoodsCategory, SPU, SPUSpecification
from meiduo_admin.serializers.skus import SKUGoodsSerializer, SKUCategorieSerializer, SPUSimpleSerializer, \
    SPUSpecSerialzier
from meiduo_admin.utils import PageNum


class SkuView(ModelViewSet):
    #指定序列化器
    serializer_class = SKUGoodsSerializer

    #指定分页器
    pagination_class = PageNum
    #指定权限
    permission_classes = [IsAdminUser]

    #重写get_queryset方法
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword == '' or keyword is None:
            return SKU.objects.all()
        else:
            return SKU.objects.filter(name=keyword)

#获取三级分类
class SKUCategorieView(ListAPIView):
    serializer_class = SKUCategorieSerializer
    queryset = GoodsCategory.objects.filter(parent_id__gt=37)

# 获取spu表名称信息
class SPUSimpleView(ListAPIView):
    serializer_class = SPUSimpleSerializer
    queryset = SPU.objects.all()

#获取spu商品规格信息

class SPUSpecView(ListAPIView):
    serializer_class = SPUSpecSerialzier
    #重写get_queryset方法
    def get_queryset(self):
        #获取spu_id
        pk = self.kwargs['pk']
        return SPUSpecification.objects.filter(spu_id=pk)

