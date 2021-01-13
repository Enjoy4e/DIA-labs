from django.db import models
from django.urls import reverse
# Create your models here.
class Supplier(models.Model):
    name = models.CharField('Название поставщика' ,max_length=50)
    field = models.CharField('Поставляемый товар' ,max_length=500)
    adress = models.CharField('Адрес поставщика' ,max_length=500, default="")
    def __str__(self):
        return self.name

class Dealer(models.Model):
    name = models.CharField('Марка автомобиля' ,max_length=50)
    number = models.CharField('Контактный номер' ,max_length=50, default=1)
    suppliers= models.ManyToManyField(Supplier, blank=True)
    def __str__(self):
        return self.name

class Car_model(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    name = models.CharField('Название модели',max_length=50)
    quantity = models.IntegerField('Количество' ,max_length=1000)
    price = models.IntegerField('Цена' ,max_length=100000)
    description = models.CharField('Описание' ,max_length=1000)
    def __str__(self):
        return self.name



