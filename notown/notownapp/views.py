from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms import forms
from notownapp.forms import *

import re

def index(request):
	return HttpResponse("Hello, world. You're at the notown index.")

"""
def form_test(request):
	mform = SongAppearsForm()
	return render(request,'notownapp/form_test.html',{'MusiciansForm': mform})

#def search_normal(re)
"""


class MusiciansList(ListView):
	model = Musicians
	context_object_name = 'musicians'

class MusiciansCreate(CreateView):
	model = Musicians
	success_url = reverse_lazy('musicians_list')
	#context_object_name = 'musicians'
	fields = '__all__'

class MusiciansUpdate(UpdateView):
	model = Musicians
	success_url = reverse_lazy('musicians_list')
	#context_object_name = 'musicians'
	fields = '__all__'

	def form_valid(self,form):
		#print form
		#print form.cleaned_data
		#print form.cleaned_data['ssn']
		#print type(form.cleaned_data['ssn'])
		#print ((re.search('[a-zA-Z]', form.cleaned_data['ssn'])) == None)

		if(((re.search('[a-zA-Z]', form.cleaned_data['ssn'])) != None)):
			print "Enter numbers"
			return HttpResponseRedirect(reverse_lazy('musicians_list'))
		return super(MusiciansUpdate, self).form_valid(form)

class MusiciansDelete(DeleteView):
	model = Musicians
	success_url = reverse_lazy('musicians_list')
	#context_object_name = 'musicians'
	fields = '__all__'

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430":
			return HttpResponseRedirect(reverse_lazy('musicians_list'))

		return super(MusiciansDelete, self).post(request, *args, **kwargs)

class PlaysList(ListView):
	model = Plays
	context_object_name = 'plays'

class PlaysCreate(CreateView):
	model = Plays
	success_url = reverse_lazy('plays_list')
	fields = '__all__'

class PlaysUpdate(UpdateView):
	model = Plays
	success_url = reverse_lazy('plays_list')
	fields = '__all__'

	def get_object(self):
		print self.kwargs
		SSN,INSTRLD = self.kwargs['pk'].split("P")
		return Plays.objects.get(ssn=SSN,instrld=INSTRLD)
#


class PlaysDelete(DeleteView):
	model = Plays
	success_url = reverse_lazy('plays_list')
	fields = '__all__'
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430":
			return HttpResponseRedirect(reverse_lazy('plays_list'))

		return super(PlaysDelete, self).post(request, *args, **kwargs)

	def get_object(self):
		print self.kwargs
		SSN,INSTRLD = self.kwargs['pk'].split("P")
		return Plays.objects.get(ssn=SSN,instrld=INSTRLD)
