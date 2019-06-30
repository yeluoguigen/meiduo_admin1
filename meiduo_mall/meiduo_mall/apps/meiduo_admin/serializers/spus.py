from rest_framework import serializers
from goods.models import SpecificationOption, SPUSpecification, SPU, Brand, GoodsCategory


class SPUGoodsSerialzier(serializers.ModelSerializer):
    '''
    SPU表序列化器
    '''
    #一级分类id
    category1_id = serializers.IntegerField()
    # 一级分类id
    category2_id = serializers.IntegerField()
    # 一级分类id
    category3_id = serializers.IntegerField()
    #关联的品牌id
    brand_id = serializers.IntegerField()
    #关联的品牌，名称
    brand = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SPU
        exclude = ('category1','category2','category3')

class SPUBrandsSerizliser(serializers.ModelSerializer):
    '''
    SPU表品牌序列化器
    '''

    class Meta:
        model = Brand
        fields = '__all__'


class CategorysSerizliser(serializers.ModelSerializer):
    '''
    SPU表分类信息序列化器
    '''

    class Meta:
        model = GoodsCategory
        fields = '__all__'
