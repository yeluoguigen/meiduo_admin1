from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
class PermissionSerializer(serializers.ModelSerializer):
    '''
    权限表序列化器
    '''
    class Meta:
        model = Permission
        fields = '__all__'

class ContentTypeSerializer(serializers.ModelSerializer):
    '''
     权限表的序列化
    '''
    name = serializers.CharField(read_only=True)
    class Meta:
        model = ContentType
        fields = '__all__'