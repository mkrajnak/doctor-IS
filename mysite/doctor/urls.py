from django.urls import path
from django.conf.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.get_doctors, name='get_doctors'),
    path('add_department/', views.add_department, name='add_department'),
    path('add_room_type/', views.add_room_type, name='add_room_type'),
    path('add_room/', views.add_room, name='add_room'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_nurse/', views.add_nurse, name='add_nurse'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_drugs/', views.add_drugs, name='add_drugs'),
    path('add_treatments/', views.add_treatments, name='add_treatments'),
    path('add_visits/', views.add_visits, name='add_visits'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
