from datetime import date, timedelta

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import GoodsVisitCount
from meiduo_admin.utils import GoodsSerializer
from users.models import User

#1 用户总量
class UserTotalCountView(APIView):
    #指定管理员权限
    permission_classes = [IsAdminUser]
    def get(self,request):
        #获取当前日期
        now_date = date.today()
        #获取所有用户
        count = User.objects.all().count()
        return Response({
            'count':count,
            'date': now_date

        })


#2 日增用户
class UserDayCountView(APIView):
    def get(self,request):
        # 指定管理员权限
        permission_classes = [IsAdminUser]
        #获取当前日期
        now_date = date.today()
        #获取当日注册用户
        count = User.objects.filter(date_joined__gte=now_date).count()
        return Response({
            'count':count,
            'date': now_date
        })

#3日活用户
class UserActiveCountView(APIView):
    #指定管理员权限
    permission_classes = [IsAdminUser]
    def get(self,request):
        #获取当日日期
        now_date = date.today()
        #获取当天登录人数
        count = User.objects.filter(last_login__gte=now_date).count()
        return Response({
            'count':count,
            'date': now_date
        })

#4日下单用户
class UserOrderCountView(APIView):
    #指定管理员权限
    permission_classes = [IsAdminUser]
    def get(self,request):
        #获取当日日期
        now_date = date.today()
        #获取当日订单创建时间
        users = User.objects.filter(orders__create_time__gte=now_date)
        user = set(users)
        count = len(user)
        return Response({
            'count':count,
            'date': now_date
        })

#5月增用户
class UserMonthCountView(APIView):
    #指定管理员权限
    permission_classes = [IsAdminUser]
    def get(self,request):
        now_date = date.today()
        #获取一个月前日期
        start_date = now_date - timedelta(29)
        date_list = []
        for i in range(30):
            #循环遍历获取当前的日期
            index_date = start_date + timedelta(days=i)
            #指定下一天日期
            cur_date = start_date + timedelta(days=i+1)
            count = User.objects.filter(date_joined__gte=index_date,date_joined__lt=cur_date).count()
            date_list.append({
                'count': count,
                'date': index_date
            })
        return Response(date_list)


#6 日分类商品数量
class GoodsDayView(APIView):
    # 指定管理员权限
    permission_classes = [IsAdminUser]
    def get(self,request):
        #获取当天日期
        now_date = date.today()
        #获取当天访问的商品分类数量信息
        goods = GoodsVisitCount.objects.filter(date__gte=now_date)
        # data_list = []
        # for good in goods:
        #     count = good.count
        #     #获取关联分类对象的名字
        #     category = good.category.name
        #     data_list.append(({'count':count,'category':category}))
        #     #返回数量
        # return Response(data_list)

        ser = GoodsSerializer(goods,many=True)
        return Response(ser.data)