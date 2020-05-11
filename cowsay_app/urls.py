from django.urls import path
from cowsay_app import views


urlpatterns = [path('', views.inputview, name='home')]
