from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('iletisim/', views.contact, name='iletisim'),
]