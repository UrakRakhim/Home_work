from django.shortcuts import render
from django.http import HttpResponse,request
from .models import Watch_film

def  Home (request):
    context = {
        'Top_films': Watch_film.objects.all()
    }
    return render(request,'Watch_film/Home.html',context)

def Music(request):
    return render(request,'Watch_film/Music.html',{'title':'Music'})



# def  Home (request):
#     return HttpResponse('<p>Dimash</p>')
# def Top_film(request):
#     return HttpResponse('<h1>IT is for TOP-10 films</h1>')