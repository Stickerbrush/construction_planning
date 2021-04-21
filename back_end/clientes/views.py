from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def saludo(req,mensaje):
    return JsonResponse({'saludo':mensaje})
    

def despedida(req):
    return JsonResponse({'despedida':'adios'})