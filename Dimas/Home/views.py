from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,request
from .models import Projects
# from .models import News
def  main(request):
	contexts={'Projects':Projects.objects.all()
	}
	return  render(request,'Home/home.html',context,{'title':'Main'})