from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SPUSpecification, SPU
from meiduo_admin.serializers.specs import SpecSerializer, SPUSerializer
from meiduo_admin.utils import PageNum


class SpecView(ModelViewSet):
    '''
    规格表的增删改查
    '''
    #指定序列化器
    serializer_class = SpecSerializer

    #指定查询集
    queryset = SPUSpecification.objects.all()

    #指定分页器
    pagination_class = PageNum
    #指定权限
    permission_classes = [IsAdminUser]

    def simple(self,request):
        spus = SPU.objects.all()
        ser = SPUSerializer(spus,many=True)
        return Response(ser.data)











