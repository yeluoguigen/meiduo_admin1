from django.conf import settings
from fdfs_client.client import Fdfs_client
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SPU, Brand, GoodsCategory
from meiduo_admin.serializers.spus import SPUGoodsSerialzier, SPUBrandsSerizliser, CategorysSerizliser
from meiduo_admin.utils import PageNum


class SPUGoodsView(ModelViewSet):
    #指定序列化器
    serializer_class = SPUGoodsSerialzier
    #指定查询集
    queryset = SPU.objects.all()
    #指定分页
    pagination_class = PageNum

    def brand(self,request):
        #1,查询所有品牌数据
        data = Brand.objects.all()
        #2 序列化返回品牌数据
        ser = SPUBrandsSerizliser(data,many=True)
        return Response(ser.data)

    def channel(self,request):
        #获取一级分类数据
        data = GoodsCategory.objects.filter(parent=None)
        ser = CategorysSerizliser(data,many=True)
        return Response(ser.data)

    def channels(self,request,pk):
        #获取二级三级分类数据
        data = GoodsCategory.objects.filter(parent_id=pk)
        #序列化
        ser = CategorysSerizliser(data,many=True)
        return Response(ser.data)
    @action(methods=['POST'],detail=False)
    def images(self,request):
        '''
        保存图片
        :param request:
        :return:
        '''
        #获取图片数据
        data = request.FILES.get('image')
        #验证图片数据
        if data is None:
            return Response(status=500)
        #2 建立连接对象
        client = Fdfs_client(settings.FASTDFS_CONF)
        #3 上传图片
        res = client.upload_by_buffer(data.read())
        #4判断上传状态
        if res['Status'] != 'Upload successed.':
            return Response({'error':'上传失败'},status=501)

        #5获取上传图片的路径
        image_url = res['Remote file_id']

        #6结果返回
        return Response({
            'img_url': settings.FDFS_URL+image_url
        },
            status=201
        )
