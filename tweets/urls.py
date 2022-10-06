from django.urls import path
from .views import tweets_check, webscrap_func

urlpatterns = [
    path('', tweets_check, name = 'tweetscheck'),
    path('web', webscrap_func, name = 'webscrap')
]