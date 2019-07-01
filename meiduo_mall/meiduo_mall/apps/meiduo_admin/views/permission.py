from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.serializers.permission import PerssionSerializer, ContentTypeSerializer
from meiduo_admin.utils import PageNum


class PermissionView(ModelViewSet):
    '''
    权限表的增删改查
    '''
    serializer_class = PerssionSerializer
    queryset = Permission.objects.all()
    pagination_class = PageNum
    permission_classes = [IsAdminUser]


    def content_types(self,request):
        contenttype = ContentType.objects.all()
        ser = ContentTypeSerializer(contenttype,many=True)
        return Response(ser.data)

