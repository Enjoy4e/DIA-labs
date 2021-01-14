from django.urls import path
from . import views


app_name = 'carshowroom'
urlpatterns = [
    path('', views.cars, name ="home"),
    path('report/',views.report, name = "report"),
    path('suppliers/', views.supply, name="supply"),
    path('edit-page', views.edit_page, name="edit_page"),
    path('update-page/<int:pk>', views.update_page, name="update_page"),
    path('delete-page/<int:pk>', views.delete_page, name="delete_page"),
]