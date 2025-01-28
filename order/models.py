from django.db import models
from django.db.models import Sum
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()


class Table(models.Model):
    number = models.IntegerField()

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

    def __str__(self) -> str:
        return str(self.number)


class Food(models.Model):
    title = models.CharField(verbose_name='Блюдо',
                             max_length=100)
    price = models.IntegerField(verbose_name='Цена',
                                validators=[MinValueValidator(0),])
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self) -> str:
        return self.title


class Order(models.Model): 
    food = models.ManyToManyField(Food, through='OrderDetail')
    all_price = models.IntegerField(blank=True, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    @property
    def all_price(self):
        return self.details.aggregate(Sum('price'))['price__sum']

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'    

    def __str__(self) -> str:
        return f'Заказ No{self.id}'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,
                                   validators=[MinValueValidator(1),])
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Заказ Детально'
        verbose_name_plural = 'Заказы Детально'

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.food.price
        super(OrderDetail, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Заказ No{self.order.id} - {self.food.title} - {self.quantity} - {self.price}'
