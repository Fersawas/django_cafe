from django import forms
from order.models import Order, OrderDetail


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table']

        widgets = {
            'table': forms.Select(attrs={'class': 'form-control', 'id': 'table_id'}),
        }


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['food', 'quantity']

        widgets = {
            'food': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min':1}),
        }
