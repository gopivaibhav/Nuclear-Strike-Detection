from django.http import HttpResponse, JsonResponse
from .models import Tweets
import webscrap

def webscrap_func(request):
    if request.method == 'GET':
        data = Tweets.objects.all()
        obj = {'time':data[len(data)-1].time, 'chance': data[len(data)-1].striked}
        web = call_web()
        print(web)
        return JsonResponse(obj, safe=False)

def call_web():
    tweet = Tweets(
        striked = webscrap.nuke_func()
    )
    tweet.save()
    return tweet

def index(request):
    return HttpResponse("Server is Up and Running")