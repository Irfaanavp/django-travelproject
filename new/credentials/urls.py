from . import views
from django.urls import path

urlpatterns = [
    path('registr', views.register, name='registr'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout')
]
