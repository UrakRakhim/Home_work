from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# from django.views.generic import TemplateView

from . forms import Login

# Create your views here.
def get_name(request):
	template_name='Register/base.html'
	context={}
	if request.method == 'POST':
		form = Login(request.POST)
		if form.is_valid():
			return redirect('https://kaspi.kz/entrance/Entrance/')
	else:
		form = Login()
		context['Error']='У Вас где-то ошибка'

	return render(request,'Register/base.html', {'form': form},context)

def main(request):
	return render(request,'Register/reg.html')