from django.conf import settings
from fdfs_client.client import Fdfs_client
from rest_framework import serializers
from goods.models import SKUImage, SKU
from celery_tasks.detail_html.tasks import get_detail_html


class ImageSerializer(serializers.ModelSerializer):
    '''
    图片表序列化器
    '''
    #关联嵌套序列化返回
    sku = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SKUImage
        fields = ('id','image','sku')

    #重写create方法，上传图片到Fdfs,
    def create(self, validated_data):
        #self.context 属性是字典数据，含有request
        sku_id = self.context['request'].data.get('sku')
        #获取保存的图片数据
        image_data = validated_data.get('image')
        #建立FastDFS的连接对象
        client = Fdfs_client(settings.FASTDFS_CONF)
        #上传图片数据
        #image_data.read() 获得图片的二进制数据
        res = client.upload_by_buffer(image_data.read())
        #判断上传状态
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError('图片上传失败')
        #上传成功返回图片的路径信息
        img_url = res['Remote file_id']
        #将路径信息保存在数据表中
        image = SKUImage.objects.create(image=img_url,sku_id=sku_id)
        #调用详情页静态化的方法
        sku_id = image.sku_id
        get_detail_html.delay(sku_id)
        #返回图片表对象
        return image

    def update(self, instance, validated_data):
        #获取保存的图片数据
        image_data = validated_data.get('image')
        #建立FastDFS的连接对象
        client = Fdfs_client(settings.FASTDFS_CONF)
        #上传图片数据
        res = client.upload_by_buffer(image_data.read())
        #判断上传状态
        if res['Status'] != 'Upload successed.':
            return serializers.ValidationError('图片上传失败')
        #上传成功
        image_url = res['Remote file_id']
        #更新图片路径
        instance.image=image_url
        instance.save()
        return instance



#1 增加图片sku序列化器
class SkuSerializer(serializers.ModelSerializer):

    class Meta:

        model = SKU
        fields = ['id','name']

