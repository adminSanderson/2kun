# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('board/<slug:slug>/', views.board_detail, name='board_detail'),
]