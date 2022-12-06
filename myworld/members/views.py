from django.shortcuts import render

# Create your views here.
# below is from w3school Django tutorial
from django.http import HttpResponse
from django.template import loader
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  #Creates an object containing the mymember object.
  context = {
    'mymembers': mymembers, 
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))