from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('listdata/',views.home, name='home'),
    path('<str:name>/',views.recepi, name='home'),
]
