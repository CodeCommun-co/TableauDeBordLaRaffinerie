from django.urls import path
from . import views

urlpatterns = [
    path('', views.tab_budgets, name='tab_budgets'),
    path('tresorie/', views.plan_tresorie, name='tresorie'),
    path('subventions/', views.suivi_subvention, name='subventions')
]
