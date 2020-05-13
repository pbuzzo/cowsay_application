from django import forms
from cowsay_app.models import CowsayInput

class CowsayAddForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
