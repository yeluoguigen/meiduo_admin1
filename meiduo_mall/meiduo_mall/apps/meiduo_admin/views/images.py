
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.serializers.images import ImageSerializer, SkuSerializer

from meiduo_admin.utils import PageNum


class ImageView(ModelViewSet):
    '''
    图片表的增删改查
    '''
    # 指定查询集
    queryset = SKUImage.objects.all()
    # 指定序列化器
    serializer_class = ImageSerializer
    #指定分页器
    pagination_class = PageNum
    # 指定权限
    permission_clasess = [IsAdminUser]
    #在保存图片之前先获取sku数据

    def simple(self,request):
        skus = SKU.objects.all()
        ser = SkuSerializer(skus,many=True)
        return Response(ser.data)



