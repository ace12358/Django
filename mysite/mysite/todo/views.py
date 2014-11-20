from django.shortcuts import render
from django import forms
from models import *

# Create your views here.

class TodoSearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, label='keyword')
    include_finished = forms.BooleanField(required=False, label='including TODO solved')
    category =  forms.ModelChoiceField(Category.objects.all(), required=False, label='Category')

#admin.site.register(TodoSearchForm)
