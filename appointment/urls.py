from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/', views.slotsOpen, name='slots'),
    path('result/', views.book, name='result')
]
