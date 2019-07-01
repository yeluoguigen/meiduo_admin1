from django.contrib.auth.models import Group, Permission
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.groups import GroupSerializer
from meiduo_admin.utils import PageNum
from meiduo_admin.serializers.permission import PermissionSerializer

class GroupView(ModelViewSet):
    '''
    用户组权限的增删改查
    '''
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    pagination_class = PageNum
    permission_classes = [IsAdminUser]

    def simple(self,requset):
        #1 查询所有权限类型
        permission = Permission.objects.all()
        ser = PermissionSerializer(permission,many=True)
        return Response(ser.data)