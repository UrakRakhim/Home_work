from . import views
from django.urls import path

urlpatterns = [
    path('',views.Home,name='Watch_film_home'),
    path('Music/',views.Music,name='Music'),
   
]

