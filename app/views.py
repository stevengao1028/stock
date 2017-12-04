# coding=utf-8
from django.shortcuts import render
import json
from django.core  import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'machine/index.html')

@csrf_exempt
def history(request):
    if request.method == "POST":
        searchtext = request.POST['searchtext']
        if searchtext == "":
            result = Profit.objects.filter(year__gt=2013)
            # print json.dumps(result)
            # server= serializers.serialize("json",result)
            # return  HttpResponse(json.dumps(result),content_type="application/json")
            return HttpResponse(json.dumps(result), content_type="application/json")
        else:
            result = Profit.objects.filter(year__gt=2013)
            # print result
            # server = serializers.serialize("json", result)
            print json.dumps(result)
            return HttpResponse(json.dumps(result), content_type="application/json")