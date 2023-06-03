from django.urls import path
from . import views


urlpatterns = [
    path('raffineurs/', views.rraffineurs, name='raffineurs')
]
