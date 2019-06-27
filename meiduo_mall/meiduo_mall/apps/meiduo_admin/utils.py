from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from goods.models import GoodsVisitCount


def jwt_response_payload_handler(token,user=None,request=None):
    '''
    自定义认证成功返回数据
    :param token:
    :param user:
    :param request:
    :return:
    '''
    return {
        "token": token,
        'id': user.id,
        'username': user.username
    }


class GoodsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = GoodsVisitCount
        fields = ('count','category')


#自定义分页器
class PageNum(PageNumberPagination):
    #指定从前端获取页容量的参数名
    page_size_query_param = 'pagesize'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'lists': data,
            'page': self.page.number,
            'pages': self.page.paginator.num_pages,
            'pagesize':self.max_page_size

        })