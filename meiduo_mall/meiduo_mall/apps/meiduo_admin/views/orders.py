from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from meiduo_admin.serializers.orders import OrderSerializer
from meiduo_admin.utils import PageNum
from orders.models import OrderInfo


class OrderView(ReadOnlyModelViewSet):
    '''
    获取多个和获取一个订单
    '''
    serializer_class = OrderSerializer
    pagination_class = PageNum
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword == '' or keyword is None:
            return OrderInfo.objects.all()
        else:
            #模糊查询
            return OrderInfo.objects.filter(order_id__contains=keyword)
    @action(methods=['put'],detail=True)
    def status(self,request,pk):
        #1 查询订单对象
        try:
            order = OrderInfo.objects.get(order_id=pk)
        except:
            return Response({'error':'无效的订单编号'})
        #2 修改订单状态
        status = request.data.get('status')
        if status is None:
            return Response({'error':'缺少订单状态'})
        order.status = status
        order.save()
        #3返回订单信息
        ser = self.get_serializer(order)
        return Response(ser.data)
