from django.urls import path
from cowsay_app import views


urlpatterns = [
    path('', views.inputview, name='home'),
    path('most_recent/', views.most_recent, name="most_recent")
]
