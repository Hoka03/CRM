from django.urls import path

from .views import PaymentListView, PaymentCreateView, PaymentDeleteView, PaymentUpdateView


urlpatterns = [
    path('pay-collection/', PaymentListView.as_view(), name='pay_collection'),
    path('add/', PaymentCreateView.as_view(), name='payment_add'),
    path('payment-edit/<int:pk>/', PaymentUpdateView.as_view(), name='payment_edit'),
    path('payment-delete/<int:pk>/', PaymentDeleteView.as_view(), name='payment_delete'),
]