from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('main/first_page/', views.first_page),
    path('main/second_page', views.second_page),
    path('main/about/', views.about)
]