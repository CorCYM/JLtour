from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('index/', views.index),
    path('testing/', views.testing),
    path('resulting/', views.resultcheck),
    path('result/', views.result),
    
    path('city_list/',views.getCityList),
    path('detail_list/',views.getDetailList),
    path('select/',views.select),
    path('citycheck1/',views.citycheck1),
    path('citycheck2/',views.citydetailJoin),
    path('citycheck3/',views.citydetailJoincheck),
    path('jltour2/', views.JLtour2),
    path('profile/', views.profile),
    path('calendar/', views.calendar),
]
