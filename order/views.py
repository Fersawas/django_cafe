from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from order.models import Order, OrderDetail, Table, Food
from order.forms import OrderForm, OrderDetailForm


user = get_user_model()


class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'

    def get_queryset(self) -> QuerySet[Any]:
        return Order.objects.filter(user=self.request.user)


class OrderView(DetailView):
    model = Order

    def get_queryset(self) -> QuerySet[Any]:
        return get_object_or_404(Order, pk=self.kwargs['pk'], user=self.request.user)


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        OrderDetailFormSet = modelformset_factory(OrderDetail, form=OrderDetailForm, extra=1)
        
        if self.request.method == 'POST':
            context['formset'] = OrderDetailFormSet(self.request.POST)
        else:
            context['formset'] = OrderDetailFormSet(queryset=OrderDetail.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        detail_formset = context['formset']
        if form.is_valid():
            print('YEP')
            order = form.save(commit=False)
            order.user = self.request.user
            order.save()
            print(detail_formset)
            details = detail_formset.save(commit=False)
            for detail in details:
                detail.order = order
                print('create detail')
                print(detail.order)
                detail.save()
            return redirect('orders:order-list')
        return self.form_valid(form)


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:order-list')
    template_name = 'order/order_form.html'
    form_class = OrderForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
