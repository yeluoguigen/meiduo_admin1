
from rest_framework import serializers
from orders.models import OrderInfo,OrderGoods
from goods.models import SKU

class SKUSerializer(serializers.ModelSerializer):
    '''
    sku
    '''
    class Meta:
        model = SKU
        fields = ('name','default_image')


class OrderGoodsSerialzier(serializers.ModelSerializer):
    '''
    订单商品表
    '''
    sku = SKUSerializer()
    class Meta:
        model = OrderGoods
        fields = ('count','price','sku')


class OrderSerializer(serializers.ModelSerializer):
    '''
    订单表序列化
    '''
    user = serializers.StringRelatedField(read_only=True)
    address = serializers.PrimaryKeyRelatedField(read_only=True)
    skus = OrderGoodsSerialzier(many=True)
    class Meta:
        model = OrderInfo
        fields = '__all__'
