from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token


from meiduo_admin.views import statistical, users, specs, images, skus

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


    # 规格选项表的增删改查
    # url(r'^goods/simple/$', specs.SpecView.as_view({'get':'simple'})),

    #商品图片表管理
    url(r'^skus/simple/$', images.ImageView.as_view({'get': 'simple'})),
    #商品三级分类
    url(r'^skus/categories/$', skus.SKUCategorieView.as_view()),
    #spu表名称
    url(r'^goods/simple/$', skus.SPUSimpleView.as_view()),

    #spu商品规格信息
    url(r'goods/(?P<pk>\d+)/specs/$',skus.SPUSpecView.as_view()),

]
#---------------------------商品图片表管理---------------------------
router = DefaultRouter()
router.register('skus/images',images.ImageView,base_name='image')
urlpatterns += router.urls

#---------------------------SKU表的增删改查--------------------------
router = DefaultRouter()
router.register('skus',skus.SkuView,base_name='sku')
urlpatterns += router.urls

#--------------------------规格管理----------------------------------
router = DefaultRouter()
router.register('goods/specs',specs.SpecView,base_name='spec')
urlpatterns += router.urls








