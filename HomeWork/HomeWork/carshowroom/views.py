import operator

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Dealer
from .models import Car_model
from .models import Supplier

def index(request):
    auto_list = Dealer.objects.all()
    context = {'auto_list': auto_list}
    return render(request, 'carshowroom/main.html', context)

def cars(request):
    auto = Car_model.objects.all().select_related('dealer')
    dealers = Dealer.objects.all()
    dealersstr = []
    for d in dealers:
        dealersstr.append(d)
    order = {key: i for i, key in enumerate(dealersstr)}
    auto_model = sorted(auto, key=lambda auto: order.get(auto.dealer, 0))
    return render(request, 'carshowroom/main.html',{'auto_model': auto_model})

def report(request):
    auto = Car_model.objects.all().select_related('dealer')
    dealers = Dealer.objects.all()
    dealersstr = []
    for d in dealers:
        dealersstr.append(d)
    order = {key: i for i, key in enumerate(dealersstr)}
    auto_model = sorted(auto, key=lambda auto: order.get(auto.dealer, 0))
    return render(request, 'carshowroom/view.html',{'auto_model': auto_model})

def supply(request):
    dealers = Dealer.objects.all().prefetch_related('suppliers')
    return render(request, 'carshowroom/supply.html',{'dealers': dealers})
