from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_view(request):
    output = "Welcome to my site."
    return HttpResponse(output)