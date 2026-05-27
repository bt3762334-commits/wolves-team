from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('join/', views.join, name='join'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('field/<str:name>/', views.field_detail, name='field_detail'),
]