# <appname>/urls.py
from django.urls import path
from .views import recipe_list, recipe_1, recipe_2, index

urlpatterns = [
    path('',index, name='index'),
    path('recipe/list',recipe_list,name='recipe list'),
    path('recipe/1',recipe_1,name='recipe 1'),
    path('recipe/2',recipe_2,name='recipe 2'),
]

# This might be needed, depending on your Django version app_name = "<appname>"
app_name = "ledger"