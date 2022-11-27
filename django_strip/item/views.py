from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, TemplateView


# Create your views here.
class ProductListView(ListView):
    pass


class ProductCreateView(CreateView):
    pass


class ProductDetailView(DetailView):
    pass


@csrf_exempt
def create_checkout_session(request, id):
    pass


class PaymentSuccessView(TemplateView):
    pass


class PaymentFailedView(TemplateView):
    pass


class OrderHistoryListView(ListView):
    pass
