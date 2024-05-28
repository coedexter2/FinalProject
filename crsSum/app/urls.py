from django.urls import path
from . import views

urlpatterns = [
    path('', views.input),
    path('wait/', views.waiting, name='waiting_name')
    
]