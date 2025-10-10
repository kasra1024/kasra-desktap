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
# --------------------------------------------------
def task_new (request): 
    task2 = list(task.objects.all()) 
    # i = [] 
    # for x in task : 
    #     i.append(x.title)
    context = {"list_task" : task2} 
    return render(request , 'product/start.html' , context)