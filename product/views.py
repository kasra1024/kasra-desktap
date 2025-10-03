from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from product.models import task


def len2(text) : 
    return len(text) 

def home (request) :
    x = task.objects.all()
    titles = []
    for i in x : 
       l = len2(i.title)
       titles.append(str (l))
    new = ",".join(titles)
    return HttpResponse(new)
# ---------------------------------------------
# def home (request) : 
#     x = task.objects.all()
#     titles = []
#     # l = len(titles)
#     for i in x : 
#        titles.append(len(i.title))
#     #    l = len(titles)
#     # new = ",".join(l)
#     return HttpResponse(titles)
    
#    ----------------------------------

