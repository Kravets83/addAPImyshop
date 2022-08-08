import json

import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from basket.basket import Basket
from orders.views import payment_confirmation
from core.settings import SECRET_KEY_PAY

@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.total_amount())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = SECRET_KEY_PAY
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None
    print('hvjgvjv')

    try:
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    if event.type == 'payment_internet_succeeded':
        payment_confirmation(event.data.object.client_secret)

    else:
        print('not correct TYPE')

    return HttpResponse(status=200)

def order_placed(reqest):
    basket = Basket(reqest)
    basket.clear()
    return render(reqest, 'payment/orderplaced.html')
