from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('index/', views.index),
    path('testing/', views.testing),
    
    path('city_list/',views.getCityList),
    path('detail_list/',views.getDetailList),
    path('select/',views.select),
    path('citycheck1/',views.citycheck1),
]
