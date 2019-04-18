from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.get_doctors, name='get_doctors'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='doctors/login.html')),
]
