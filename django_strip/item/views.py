import json

import stripe as stripe
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, TemplateView

from django_strip import settings
from item.models import Item, Order


# Create your views here.
class ItemListView(ListView):
    model = Item
    template_name = "item/item_list.html"
    context_object_name = 'item_list'


class ItemCreateView(CreateView):
    model = Item
    fields = '__all__'
    template_name = "item/item_create.html"
    success_url = reverse_lazy("home")


class ItemDetailView(DetailView):
    model = Item
    template_name = "item/item_detail.html"
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


class CreateCheckoutSession(View):
    def get(self, request, id, *args, **kwargs):
        request_data = json.loads(request.body)
        product = get_object_or_404(Item, pk=id)

        stripe.api_key = settings.STRIPE_SECRET_KEY
        checkout_session = stripe.checkout.Session.create(
            customer_email=request_data['email'],
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': product.name,
                        },
                        'unit_amount': int(product.price * 100),
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=request.build_absolute_uri(
                reverse('success')
            ) + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.build_absolute_uri(reverse('failed')),
        )
        order = Order()
        order.customer_email = request_data['email']
        order.product = product
        order.stripe_payment_intent = checkout_session['payment_intent']
        order.amount = int(product.price * 100)
        order.save()
        return JsonResponse({'sessionId': checkout_session.id})


class PaymentSuccessView(View):
    template_name = "item/payment_success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        order = get_object_or_404(Order, stripe_payment_intent=session.payment_intent)
        order.has_paid = True
        order.save()
        return render(request, self.template_name)


class PaymentFailedView(TemplateView):
    template_name = "item/payment_failed.html"


class OrderHistoryListView(ListView):
    model = Order
    template_name = "item/order_history.html"
