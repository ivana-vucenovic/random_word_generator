from django.urls import path 
from . import views

urlpatterns = [
    path('', views.random),
    path('word_generator', views.submit),
    path('reset', views.reset)
]

