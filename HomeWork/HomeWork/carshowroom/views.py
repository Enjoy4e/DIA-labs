import operator
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Dealer
from .models import Car_model
from .models import Supplier
from .forms import ArticleForm
from django.urls  import reverse

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

def edit_page(request):
    success = False
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    list_suppliers=Supplier.objects.all()
    context = {
        'list_suppliers': list_suppliers,
        'form': ArticleForm(),
        'success': success
    }
    return render(request,'carshowroom/edit-page.html',context)

def update_page(request,pk):
    get_article = Supplier.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=get_article)
        if form.is_valid():
            form.save()
    context = {
        'get_article': get_article,
        'update': True,
        'form': ArticleForm(instance=get_article),
    }
    return render(request,'carshowroom/update-page.html',context)

def delete_page(request,pk):
    get_article = Supplier.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('carshowroom:edit_page'))
