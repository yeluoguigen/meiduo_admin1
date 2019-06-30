from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SKU, GoodsCategory, SPU
from meiduo_admin.serializers.skus import SKUSerializer, GoodsCategorieSerializer, SPUSpecificationSerialzier
from meiduo_admin.utils import PageNum


class SkuView(ModelViewSet):
    #指定序列化器
    serializer_class = SKUSerializer

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

    #获取sku所有三级分类信息
    @action(methods=['get'],detail=False)
    def categories(self,request):
        #查询所有的sku数据
        goods = GoodsCategory.objects.filter(subs=None)
        ser  = GoodsCategorieSerializer(goods,many=True)
        return Response(ser.data)



    #获取spu商品规格信息
    def specs(self,request,pk):
        #根据pk值查询spu商品
        spu = SPU.objects.get(id=pk)
        #根据spu商品对象查询规格
        spec = spu.specs.all()
        #返回规格数据
        ser = SPUSpecificationSerialzier(spec,many=True)
        return Response(ser.data)




