from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from notownapp.forms import SongAppearsForm

def index(request):
	return HttpResponse("Hello, world. You're at the notown index.")

def form_test(request):
	mform = SongAppearsForm()
	return render(request,'notownapp/form_test.html',{'MusiciansForm': mform})

#def search_normal(re)
