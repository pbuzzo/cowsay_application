from django.shortcuts import render
from cowsay_app.models import CowsayInput
from cowsay_app.forms import CowsayAddForm

from collections import deque
import subprocess
# from cowpy import cow


def index(request):
    return render(request, 'index.html')


def most_recent(request):
    data = CowsayInput.objects.all()
    html = 'most_recent.html'
    q = deque(data, maxlen=10)
    stack = []
    for item in q:
        stack.append(item)

    return render(request, html, {'data': data, "stack": stack})


def inputview(request):
    html = "index.html"
    output = []
    if request.method == "POST":
        form = CowsayAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # check_output or run
            # subprocess.run(..., check=True, stdout=PIPE).stdout
            # https://stackoverflow.com/questions/14078117/how-do-you-use-subprocess-check-output-in-python
            word = CowsayInput.objects.create(
                text=(data['text']),
            )
            cow_str = subprocess.check_output(
                ['cowsay', str(data['text'])]
            ).decode('utf-8')
            # Using CowPy package ###
            # cow_cls = cow.get_cow('default')
            # cheese = cow_cls()
            # msg = cheese.milk(str(data['text']))               
            return render(
                request,
                html,
                {'form': form, 'word': word, "decoded": cow_str}
            )
    form = CowsayAddForm()
    text = CowsayInput.objects.all()

    return render(
        request,
        html,
        {'form': form, "text": text, "output": output}
    )
