from django.shortcuts import render
from django.views.generic import TemplateView


class PaymentCollectionTemplateView(TemplateView):
    template_name = 'all-fees.html'


class PaymentAddExpensesTemplateView(TemplateView):
    template_name = 'add-expense.html'