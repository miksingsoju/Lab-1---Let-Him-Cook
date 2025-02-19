from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome!</h1>")
def recipe_list(request):
    return HttpResponse("<h1>recipe list! </h1>")

def recipe_1(request):
    return HttpResponse("<h1>1 </h1>")

def recipe_2(request):
    return HttpResponse("<h1>2</h1>")