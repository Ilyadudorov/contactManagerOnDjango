from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect
# Create your views here.

def index(request): #HttpRequest
    return render(request, "index.html")

def categories(request, catid = 0):
    if(int(catid) > 99):
        raise Http404()
    else:
        return HttpResponse(f"<h1>Тестовая страница категорий номер {catid}</h1>")
    
    

def indexMain(request): 
    response = redirect('home') 
    return response 

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')