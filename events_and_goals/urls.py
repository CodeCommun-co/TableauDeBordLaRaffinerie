from django.urls import path
from . import views


urlpatterns = [
    path('event/', views.follow_event, name='event'),
    path('goals_and_results/', views.goals_and_results, name='goals_and_results'),
    path('volunteering/', views.follow_volunteering, name='volunteering')

]
