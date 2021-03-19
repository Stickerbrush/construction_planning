from django.http import HttpResponse

def hello_world(request): # First view function

    return HttpResponse("Tu gfa")