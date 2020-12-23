from django.shortcuts import get_object_or_404, render

from .models import Cinema
from .models import Description


def index(request):
    cinema_list = Cinema.objects.all()
    context = {'cinema_list': cinema_list}
    return render(request, 'shop/index.html', context)


def detail(request, cinema_id):
    cinema_list = Cinema.objects.all()
    for i in cinema_list:
        if i.id == cinema_id:
            cinema = i
    description = get_object_or_404(Description, pk=cinema_id)
    return render(request, 'shop/detail.html', {'cinema': cinema, 'description': description})
