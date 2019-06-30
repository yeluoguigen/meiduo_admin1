from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SpecificationOption, SPUSpecification
from meiduo_admin.serializers.options import OptionSerializer, OptionSpecificationSerializer
from meiduo_admin.utils import PageNum



class OptionsView(ModelViewSet):
    '''
    规格选项表的增删改查
    '''
    queryset = SpecificationOption.objects.all()
    serializer_class = OptionSerializer
    pagination_class = PageNum

    def simple(self,request):
        specs = SPUSpecification.objects.all()
        ser = OptionSpecificationSerializer(specs,many=True)
        return Response(ser.data)



