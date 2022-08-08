from django.shortcuts import render
from .models import Order,OrderItem
from basket.basket import Basket
from django.http.response import JsonResponse

def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        user_id = request.user.id
        order_key = request.POST.get('order_key')
        basket_total = basket.total_amount()
        if Order.objects.filter(order_key=order_key).exists():
            ''
        else:
            order = Order.objects.create(user_id=user_id, full_name='name', address1='add1', address2='add2',
                                         amount_pay=basket_total, order_key=order_key, billing_status=True)
            order_id = order.pk
            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'],
                                         price=item['price'], quantity=item['qty'])
        response = JsonResponse({'success': 'return ???????????'})
        return response



def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders


