from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpattern = [
    path('', views.home, name='index'),
    path('create/', views.create_account, name='create'),
    path('balance/', views.balance, name='balance'),
    path('transaction/', views.balance, name='transaction')
]