from rest_framework.generics import  ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser

from meiduo_admin.serializers.users import UserSerializer
from meiduo_admin.utils import PageNum
from users.models import User




#1获取查询用户
class UserView(ListCreateAPIView):
    #指定使用的序列化器
    serializer_class = UserSerializer
    #指定分页器
    pagination_class = PageNum
    #指定权限
    permission_classes = [IsAdminUser]

    #重写get_queryset方法根据前端传递的keyword参数，
    def get_queryset(self):
        #1 获取前端的keyword参数
        keyword = self.request.query_params.get('keyword')
        if keyword == '':
            return User.objects.filter(is_staff=False)
        else:
            #模糊查询username__contains
            return User.objects.filter(is_staff=False,username__contains=keyword)



















