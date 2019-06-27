from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views import statistical, users

urlpatterns = [
    #登录路由
    url(r'^authorizations/$', obtain_jwt_token),
    # --------数据统计---------
    #用户总量统计
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
    # 当天注册用户总量统计
    url(r'^statistical/day_increment/$',statistical.UserDayCountView.as_view()),
    #当天登录用户总量统计
    url(r'^statistical/day_active/$', statistical.UserActiveCountView.as_view()),
    #当天下单用户总量统计
    url(r'^statistical/day_orders/$', statistical.UserOrderCountView.as_view()),
    #月增用户总量统计
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    # 商品分类访问量统计
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayView.as_view()),
    #用户查询
    url(r'^users/$', users.UserView.as_view()),




]