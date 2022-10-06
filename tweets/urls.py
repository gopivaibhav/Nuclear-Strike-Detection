from django.urls import path
from .views import webscrap_func

urlpatterns = [
    path('', webscrap_func, name = 'webscrap')
]