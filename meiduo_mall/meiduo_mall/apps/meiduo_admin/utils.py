from rest_framework import serializers

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