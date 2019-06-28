from django.db import transaction
from rest_framework import serializers
from rest_framework.response import Response

from goods.models import SKU, SKUSpecification, GoodsCategory, SpecificationOption, SPUSpecification




class SKUSpecificationSerialzier(serializers.ModelSerializer):
    '''
    SKU规格表Id
    '''
    spec_id =serializers.IntegerField(read_only=True)
    option_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = SKUSpecification
        fields = ['spec_id','option_id']

class SKUGoodsSerializer(serializers.ModelSerializer):
    '''
    获取SKU详细信息的序列化器
    '''
    #指定所关联的选项信息，关联嵌套返回
    specs = SKUSpecificationSerialzier(many=True)
    #指定分类信息
    category_id = serializers.IntegerField()
    #关联嵌套
    category = serializers.StringRelatedField(read_only=True)
    #指定spu信息
    spu_id = serializers.IntegerField()
    #指定关联的spu表信息
    spu = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SKU
        fields = '__all__'

    def create(self, validated_data):
        #self 指的是当前序列化对象
        # specs = self.context['request'].data.get('specs')
        specs = validated_data['specs']
        # SKU表中没有specs字段，所以保存的时候要删除
        del validated_data['specs']
        with transaction.atomic():
            #开启事务
            sid = transaction.savepoint()
            try:
                #保存sku
                sku = SKU.objects.create(**validated_data)
                #保存sku具体规格
                for spec in specs:
                    SKUSpecification.objects.create(sku=sku,spec_id=spec['spec_id'],option_id=spec['option_id'])
            except :
                #捕获异常，说明数据库操作没有成功，进行事务回滚
                transaction.savepoint_rollback(sid)
                return serializers.ValidationError('数据库错误')
            else:
                #没有异常，进行提交
                transaction.savepoint_commit(sid)
                return Response({})






class SKUCategorieSerializer(serializers.ModelSerializer):
    '''
    商品分类序列化器
    '''
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class SPUSimpleSerializer(serializers.ModelSerializer):
    '''
    商品spu表信息序列化器
    '''
    class Meta:
        model = GoodsCategory
        fields =[ 'name','id']

class SPUOptineSerializer(serializers.ModelSerializer):
    '''
    spu商品规格选项序列化器
    '''
    class Meta:
        model = SpecificationOption
        fields = ['id','value']

class SPUSpecSerialzier(serializers.ModelSerializer):
    '''
    规格序列化器
    '''
    #关联序列化返回spu表数据
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    #关联序列化返回选项信息
    options = SPUOptineSerializer(read_only=True,many=True)
    class Meta:
        model = SPUSpecification
        fields = '__all__'





