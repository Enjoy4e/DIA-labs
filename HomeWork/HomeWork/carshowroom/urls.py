from django.urls import path
from . import views

app_name = 'carshowroom'
urlpatterns = [
    path('', views.cars, name ="home"),
    path('report/',views.report, name = "report"),
    path('suppliers/', views.supply, name="supply"),
]