from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from basket.basket import Basket
import stripe

# Create your views here.
@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.total_amount())
    total = total.replace('.', '')
    total = int(total)

    # stripe.api_key = 'https://dashboard.stripe.com/test/apikeys'
    # intent = stripe.PaymentIntent.create(
    #     amount=total,
    #     currency='gbp',
    #     metadata={'userid': request.user.id}
    # )

    return render(request, 'payment/home.html')#, {'client_secret': intent.client_secret})