from rest_framework import serializers

from goods.models import SPUSpecification, SPU


class SpecSerializer(serializers.ModelSerializer):
    '''
    商品规格表序列化器
    '''
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    class Meta:
        model = SPUSpecification
        fields = ['id','name','spu','spu_id']


class SPUSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPU
        fields = ['id','name']
