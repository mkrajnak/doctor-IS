from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.get_doctors, name='get_doctors'),
]
