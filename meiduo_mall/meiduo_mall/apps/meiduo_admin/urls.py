from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token


from meiduo_admin.views import statistical, users, specs, images, skus, options, spus, orders, permission, groups

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

    #商品图片表管理
    url(r'^skus/simple/$', images.ImageView.as_view({'get': 'simple'})),

    #spu表名称
    url(r'^goods/simple/$', specs.SpecView.as_view({'get':'simple'})),

    # ------------------sku表管理------------------
    url(r'goods/(?P<pk>\d+)/specs/$',skus.SkuView.as_view({'get':'specs'})),
    #spec表名称
    url(r'^goods/specs/simple/$', options.OptionsView.as_view({'get': 'simple'})),
    #spu品牌名称 id
    url(r'^goods/brands/simple/$', spus.SPUGoodsView.as_view({'get': 'brand'})),

    url(r'^goods/channel/categories/$', spus.SPUGoodsView.as_view({'get': 'channel'})),

    url(r'^goods/channel/categories/(?P<pk>\d+)/$', spus.SPUGoodsView.as_view({'get': 'channels'})),
    #权限类型
    url(r'^permission/content_types/$', permission.PermissionView.as_view({'get': 'content_types'})),
    #获取所有权限
    url(r'^permission/simple/$', groups.GroupView.as_view({'get': 'simple'})),

]
#---------------------------商品图片表管理---------------------------
router = DefaultRouter()
router.register('skus/images',images.ImageView,base_name='image')
urlpatterns += router.urls

#---------------------------SKU表管理-------------------------
router = DefaultRouter()
router.register('skus',skus.SkuView,base_name='sku')
urlpatterns += router.urls

#--------------------------规格管理----------------------------------
router = DefaultRouter()
router.register('goods/specs',specs.SpecView,base_name='spec')
urlpatterns += router.urls

#--------------------------规格选项管理----------------------------------
router = DefaultRouter()
router.register('specs/options',options.OptionsView,base_name='option')
urlpatterns += router.urls

#---------------------------SPU表管理-------------------------
router = DefaultRouter()
router.register('goods',spus.SPUGoodsView,base_name='good')
urlpatterns += router.urls

#---------------------------订单表管理-------------------------
router = DefaultRouter()
router.register('orders',orders.OrderView,base_name='order')
urlpatterns += router.urls

#---------------------------权限表管理-------------------------
router = DefaultRouter()
router.register('permission/perms',permission.PermissionView,base_name='permission')
urlpatterns += router.urls

#---------------------------用户组表管理-------------------------
router = DefaultRouter()
router.register('permission/groups',groups.GroupView,base_name='group')
urlpatterns += router.urls







