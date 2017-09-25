from django.http import HttpResponse
from django.shortcuts import render

# Create your views page
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
