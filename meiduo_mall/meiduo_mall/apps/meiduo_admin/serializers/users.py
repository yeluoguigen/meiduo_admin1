import re

from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','mobile','email','password']

        extra_kwargs = {
            'password':{
                'write_only': True,
                'max_length': 20,
                'min_length': 8
            },
            'username':{
                'max_length':20,
                'min_length':5
            }
        }
    #验证手机号格式
    def validate_mobile(self,value):
        if not re.match(r'1[3-9]\d{9}',value):
            return serializers.ValidationError('手机号格式不正确')
        else:
            return value

    #重写create方法,对密码加密
    def create(self,validated_data):
        #调用父类方法super()
        # user = super().create(validated_data)
        # user.set_password(validated_data['password'])
        # user.save()

        user = User.objects.create_user(**validated_data)
        return user













