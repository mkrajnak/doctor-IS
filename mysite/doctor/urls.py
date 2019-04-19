from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.get_doctors, name='get_doctors'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_room_type/', views.add_room_type, name='add_room_type'),
    path('add_room/', views.add_room, name='add_room'),
    path('accounts/', include('django.contrib.auth.urls')),
]
