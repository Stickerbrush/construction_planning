import json
from django.http import HttpResponse
from django.http import JsonResponse


def saludo(req,mensaje):
    return JsonResponse({'saludo':mensaje})
    

def despedida(req):
    return JsonResponse({'despedida':'adios'})