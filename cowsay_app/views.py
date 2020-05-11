from django.shortcuts import render
from cowsay_app.models import CowsayInput


def index(request):
    return render(request, 'index.html')


def inputview(request):
    data = CowsayInput.objects.all()
    html = 'index.html'
    return render(request, html, {'data': data})
