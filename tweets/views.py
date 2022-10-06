from django.http import HttpResponse
# import json
# from django.views.decorators.csrf import csrf_exempt
# import webscrap
# from test import make_prediction

# @csrf_exempt
def tweets_check(request):
    if request.method == 'POST':
    #     data = json.loads(request.body.decode("utf-8"))
    #     new_data = make_prediction(data['tweets'])
    #     total_length = len(new_data)
    #     count = 0
    #     for item in new_data:
    #         if(item[0] == 0):
    #             count +=1
    #         print(item, item[0], count)
    #     if(count/total_length >= 0.9):
    #         return HttpResponse("Safe!!")
    #     return HttpResponse("Not Safe bruh!!")
    # else:
        return HttpResponse('Hello Fucker!!')

def webscrap_func(request):
    print(request)
    # print(webscrap.nuke_func())
    # return HttpResponse(webscrap.nuke_func())

