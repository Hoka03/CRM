from django.urls import path

from .views import PaymentCollectionTemplateView, PaymentAddExpensesTemplateView


urlpatterns = [
    path('pay-collection/', PaymentCollectionTemplateView.as_view(), name='pay_collection'),
    path('pay-add-expense/', PaymentAddExpensesTemplateView.as_view(), name='pay_add_expense'),
]