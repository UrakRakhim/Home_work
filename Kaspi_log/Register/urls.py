from django.urls import path,include
from . import views
# from Register.views import LoginView

urlpatterns = [
    path('',views.get_name,name='Login'),
    path('reg/',views.main,name='Reg'),
]
