from django.urls import path
from . import views

urlpatterns = [
    path('', views.input),
    path('wait/', views.results, name='results_name'),    
]