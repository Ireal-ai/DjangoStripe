from django.urls import path

from item.views import (
    ItemListView,
    ItemCreateView,
    ItemDetailView,
    PaymentSuccessView,
    PaymentFailedView,
    OrderHistoryListView,
    CreateCheckoutSession,
)

urlpatterns = [
    path('', ItemListView.as_view(), name='home'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('item/<id>', ItemDetailView.as_view(), name='item'),
    path('success/', PaymentSuccessView.as_view(), name='success'),
    path('failed/', PaymentFailedView.as_view(), name='failed'),
    path('history/', OrderHistoryListView.as_view(), name='history'),

    path('buy/<id>/', CreateCheckoutSession.as_view(), name='api_checkout_session'),
]
