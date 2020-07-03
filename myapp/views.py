from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser

def get_details_ifsc(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        obj = Branches.objects.get(ifsc = data['ifsc'])
        print(obj)
        dict = {
            'ifsc' : obj.ifsc,
            'id' : obj.bank.id,
            'name' : obj.bank.name,
            'branch' : obj.branch,
            'address' : obj.address,
            'city' : obj.city,
            'district' : obj.district,
            'state' : obj.state
        }
        return JsonResponse(dict)


def get_details_name_city(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        objs = list(Branches.objects.filter(city = data['city']))
        req_objs = []
        for obj in objs:
            if obj.bank.name==data['name']:
                dict ={}
                dict = {
                    'ifsc' : obj.ifsc,
                    'id' : obj.bank.id,
                    'name' : obj.bank.name,
                    'branch' : obj.branch,
                    'address' : obj.address,
                    'city' : obj.city,
                    'district' : obj.district,
                    'state' : obj.state
                }
                req_objs.append(dict)
        print(req_objs)
        result = {
            'details' : req_objs
        }
        return JsonResponse(result)
