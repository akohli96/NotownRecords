from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from notownapp.forms import *

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
