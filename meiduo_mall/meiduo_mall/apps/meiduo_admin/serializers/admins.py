from rest_framework.serializers import ModelSerializer

from users.models import User


class AdminSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra = {
            'password':{
                'write_only':True
            }
        }
#重写父类create方法
    def create(self, validated_data):
        #添加管理员字段
        validated_data['is_staff'] = True
        #调用父类方法创建管理员用户
        admin = super().create(validated_data)
        #用户密码加密
        password = validated_data['password']
        admin.set_password(password)
        admin.save()
        return admin
