from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms import forms
from notownapp.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import ModelFormMixin

import re

def index(request):
	return HttpResponse("Welcome to Notown App")

"""
def form_test(request):
	mform = SongAppearsForm()
	return render(request,'notownapp/form_test.html',{'MusiciansForm': mform})

#def search_normal(re)
"""
#http://franklingu.github.io/programming/2016/08/29/django-class-based-views-and-access-mixins/


class Album_ProducerList(LoginRequiredMixin,ListView):
	model = Album_Producer
	context_object_name = 'album_producers'
	login_url = '/notownapp/login/'
	#redirect_field_name = '/what/'
	print "LOGIN"
	#print user.is_authenticated
	def get_queryset(self):
		print "Album Producer Queryset"

		ALBUMIDENTIFIER = self.request.GET.get("albumidentifier")
		COPYRIGHTDATE = self.request.GET.get("copyrightdate")
		TITLE = self.request.GET.get("title")
		SPEED = self.request.GET.get("speed")
		SSN = self.request.GET.get("ssn")

		print "ALBUM"
		print self.request.GET.get("albumidentifier")
		print "COPYRIGHTDATE"
		print self.request.GET.get("copyrightdate")
		print "TITLE"
		print self.request.GET.get("title")
		print "SPEED"
	 	print self.request.GET.get("speed")
		print "SSN"
		print self.request.GET.get("ssn")


		print ALBUMIDENTIFIER,COPYRIGHTDATE,TITLE,SPEED,SSN

		if (None == ALBUMIDENTIFIER and  None == COPYRIGHTDATE and None == TITLE and None ==  SPEED and None == SSN):
			print "RETURNING ALL"
			return Album_Producer.objects.all()
		else:
			queryset = Album_Producer.objects.filter(albumident__icontains=ALBUMIDENTIFIER)
			queryset = queryset.filter(copyright__icontains=COPYRIGHTDATE)
			queryset = queryset.filter(title__icontains=TITLE)
			queryset = queryset.filter(speed__icontains=SPEED)
			queryset = queryset.filter(ssn__ssn__icontains=SSN)
			print queryset
			return queryset
			#copyright, songappears, speed, ssn, ssn_id, title



class Album_ProducerCreate(LoginRequiredMixin,CreateView):
	model = Album_Producer
	success_url = "/notownapp/albumproducerslist/"
	fields = "__all__"
	login_url = '/notownapp/login/'

	def form_valid(self,form):
		#print form
		#print form.cleaned_data
		#print form.cleaned_data['ssn']
		#print type(form.cleaned_data['ssn'])
		#print ((re.search('[a-zA-Z]', form.cleaned_data['ssn'])) == None)
		print "IN FORM VALID"
		print form
		print form.cleaned_data
		if(( (form.cleaned_data['albumident'])) < 0 ):
			#raise forms.ValidationError("Enter number greater than 0")
			print "Enter number greater than 0"
			return HttpResponseRedirect("/notownapp/albumproducerslist/")
		return super(Album_ProducerCreate, self).form_valid(form)

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect("/notownapp/albumproducerslist/")

		return super(Album_ProducerCreate, self).post(request, *args, **kwargs)

class Album_ProducerUpdate(LoginRequiredMixin,UpdateView):
	model = Album_Producer
	success_url = reverse_lazy('album_producers_list')
	#context_object_name = 'musicians'
	fields = '__all__'

	def form_valid(self,form):
		#print form
		#print form.cleaned_data
		#print form.cleaned_data['ssn']
		#print type(form.cleaned_data['ssn'])
		#print ((re.search('[a-zA-Z]', form.cleaned_data['ssn'])) == None)
		print "IN FORM VALID"
		print form
		print form.cleaned_data
		if(( (form.cleaned_data['albumident'])) < 0 ):
			#raise forms.ValidationError("Enter number greater than 0")
			print "Enter number greater than 0"
			return HttpResponseRedirect("/notownapp/albumproducerslist/")
		return super(Album_ProducerUpdate, self).form_valid(form)

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('album_producers_list'))

		return super(Album_ProducerUpdate, self).post(request, *args, **kwargs)

class Album_ProducerDelete(LoginRequiredMixin,DeleteView):
	model = Album_Producer
	success_url = reverse_lazy('album_producers_list')
	#context_object_name = 'musicians'
	fields = '__all__'

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('album_producers_list'))

		return super(Album_ProducerDelete, self).post(request, *args, **kwargs)

class MusiciansList(LoginRequiredMixin,ListView):
	model = Musicians
	context_object_name = 'musicians'
	#Musicians.objects.filter(ssn__contains=853253156,name__contains="Ayush")
	login_url = '/notownapp/login/'
	def get_queryset(self):
		print "Musical Queryset"

		NAME= self.request.GET.get("name")
		SSN = self.request.GET.get("ssn")
		print NAME,SSN

		if SSN is not None and NAME is not None:
			queryset=Musicians.objects.filter(ssn__icontains=SSN)
			print queryset
			#print queryset.filter(name__contains=NAME.tolower())
			queryset = queryset.filter(name__icontains=NAME)
			print queryset
			return queryset
		else:
			return Musicians.objects.all()



class MusiciansCreate(LoginRequiredMixin,CreateView):
	model = Musicians
	success_url = reverse_lazy('musicians_list')
	#context_object_name = 'musicians'
	fields = '__all__'
	login_url = '/notownapp/login/'

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('musicians_list'))

		return super(MusiciansCreate, self).post(request, *args, **kwargs)

	def form_valid(self,form):
		#print form
		#print form.cleaned_data
		#print form.cleaned_data['ssn']
		#print type(form.cleaned_data['ssn'])
		#print ((re.search('[a-zA-Z]', form.cleaned_data['ssn'])) == None)

		if(((re.search('[a-zA-Z]', form.cleaned_data['ssn'])) != None)):
			print "Enter numbers"
			return HttpResponseRedirect(reverse_lazy('musicians_list'))
		return super(MusiciansCreate, self).form_valid(form)

class MusiciansUpdate(LoginRequiredMixin,UpdateView):
	model = Musicians
	success_url = reverse_lazy('musicians_list')
	#context_object_name = 'musicians'
	fields = '__all__'
	login_url = '/notownapp/login/'

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

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('musicians_list'))

		return super(MusiciansUpdate, self).post(request, *args, **kwargs)

class MusiciansDelete(LoginRequiredMixin,DeleteView):
	model = Musicians
	success_url = reverse_lazy('musicians_list')
	#context_object_name = 'musicians'
	fields = '__all__'
	login_url = '/notownapp/login/'

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('musicians_list'))

		return super(MusiciansDelete, self).post(request, *args, **kwargs)

class PlaysList(LoginRequiredMixin,ListView):
	model = Plays
	context_object_name = 'plays'
	login_url = '/notownapp/login/'

	def get_queryset(self):
		print "Plays Queryset"
		print self.request
		print self.request.GET
		INSTRLD= self.request.GET.get("instrld")
		SSN = self.request.GET.get("ssn")
		print INSTRLD,SSN

		if SSN is not None and INSTRLD is not None:
			queryset=Plays.objects.filter(ssn__ssn__icontains=SSN)
			print queryset
			#print queryset.filter(name__contains=NAME.tolower())
			queryset = queryset.filter(instrld__instrld__icontains=INSTRLD)
			print queryset
			return queryset
		else:
			return Plays.objects.all()



class PlaysCreate(LoginRequiredMixin,CreateView):
	model = Plays
	success_url = reverse_lazy('plays_list')
	fields = '__all__'
	login_url = '/notownapp/login/'

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('plays_list'))

		return super(PlaysCreate, self).post(request, *args, **kwargs)

class PlaysUpdate(LoginRequiredMixin,UpdateView):
	model = Plays
	success_url = reverse_lazy('plays_list')
	fields = '__all__'
	login_url = '/notownapp/login/'

	def get_object(self):
		print self.kwargs
		SSN,INSTRLD = self.kwargs['pk'].split("P")
		return Plays.objects.get(ssn=SSN,instrld=INSTRLD)

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('plays_list'))

		return super(PlaysUpdate, self).post(request, *args, **kwargs)
#


class PlaysDelete(LoginRequiredMixin,DeleteView):
	model = Plays
	success_url = reverse_lazy('plays_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('plays_list'))

		return super(PlaysDelete, self).post(request, *args, **kwargs)

	def get_object(self):
		print self.kwargs
		SSN,INSTRLD = self.kwargs['pk'].split("P")
		return Plays.objects.get(ssn=SSN,instrld=INSTRLD)

class InstrumentsList(LoginRequiredMixin,ListView):
	model = Instruments
	context_object_name = 'instruments'
	login_url = '/notownapp/login/'
	#Musicians.objects.filter(ssn__contains=853253156,name__contains="Ayush")

	def get_queryset(self):
		print "Instrument Queryset"

		INSTRLD= self.request.GET.get("instrld")
		DNAME = self.request.GET.get("dname")
		KEY = self.request.GET.get("key")
		PLAYS = self.request.GET.get("plays")
		print INSTRLD,DNAME,KEY,PLAYS

		#Instruments.objects.filter(instrld__icontains="")
		#Instruments.objects.filter(dname__icontains="")
		#Instruments.objects.filter(keys__icontains="")
		#Instruments.objects.filter(instrld__icontains="")
		#Instruments.objects.filter(plays__ssn__icontains="")

		if INSTRLD is not None and DNAME is not None and KEY is not None and PLAYS is not None:
			queryset=Instruments.objects.filter(instrld__icontains=INSTRLD)
			print queryset
			queryset = queryset.filter(dname__icontains=DNAME)
			print queryset
			queryset = queryset.filter(key__icontains=KEY)
			print queryset
			queryset = queryset.filter(plays__ssn__icontains=PLAYS)
			return queryset
		else:
			return Instruments.objects.all()


class InstrumentsCreate(LoginRequiredMixin,CreateView):
	model = Instruments
	success_url = reverse_lazy('instruments_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def form_valid(self,form):
		print "CHECKING REGEX"
		print form.cleaned_data
		if(((form.cleaned_data['instrld'] <0 ))):
			print "Enter positive"
			return HttpResponseRedirect(reverse_lazy('instruments_list'))
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('instruments_list'))

		return super(InstrumentsCreate, self).post(request, *args, **kwargs)

class InstrumentsUpdate(LoginRequiredMixin,UpdateView):
	model = Instruments
	success_url = reverse_lazy('instruments_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def form_valid(self,form):
		print "CHECKING REGEX"
		print form.cleaned_data
		if(((form.cleaned_data['instrld'] <0 ))):
			print "Enter positive"
			return HttpResponseRedirect(reverse_lazy('instruments_list'))
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('instruments_list'))

		return super(InstrumentsUpdate, self).post(request, *args, **kwargs)

class InstrumentsDelete(LoginRequiredMixin,DeleteView):
	model = Instruments
	success_url = reverse_lazy('instruments_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('instruments_list'))

		return super(InstrumentsDelete, self).post(request, *args, **kwargs)

class SongAppearsList(ListView):
	model = SongAppears
	context_object_name = 'songappears'
	success_url = reverse_lazy('songappears_list')
	fields = '__all__'

	def get_queryset(self):

		print "SongAppears Queryset"

		print str(self.request.user)

		AUTHOR = self.request.GET.get("author")
		TITLE = self.request.GET.get("title")
		NAME = self.request.GET.get("name")
		queryset = SongAppears.objects.all(	)
		print AUTHOR,TITLE,NAME
		print AUTHOR == None
		print TITLE == None
		print NAME == None
		if TITLE != None:
			#print queryset
			queryset = SongAppears.objects.filter(albumident__title__icontains=TITLE)
		if NAME != None:
			#print queryset
			queryset = queryset.filter(title__icontains=NAME)
		if AUTHOR != None:
			queryset = queryset.filter(author__name__icontains=AUTHOR)
		if str(self.request.user) ==  "staff":
			#queryset=SongAppears.objects.filter(songID__icontains=SONGID)
			#print queryset

			#PERFORMS = self.request.GET.get("performs")
			#print INSTRLD,DNAME,KEY,PLAYS
			print AUTHOR,TITLE,NAME
			SONGID= self.request.GET.get("songid")
			ALBUMIDENT=self.request.GET.get("albumident")
			PERFORMER=self.request.GET.get("performer")
			print SONGID,ALBUMIDENT,PERFORMER
			if ALBUMIDENT!= None:
				queryset = queryset.filter(albumident__albumident__icontains=ALBUMIDENT)
			if SONGID != None:
				queryset =queryset.filter(songID__icontains=SONGID)

			if PERFORMER != None:
				queryset=queryset.filter(performs__ssn__icontains=PERFORMER)

			print queryset
			return queryset
		else:
			print queryset
			return queryset

class SongAppearsUpdate(LoginRequiredMixin,UpdateView):
	model = SongAppears
	success_url = reverse_lazy('songappears_list')
	fields = '__all__'
	login_url = '/notownapp/login/'

	def form_valid(self,form):
		print "CHECKING REGEX"
		print form.cleaned_data
		if(((form.cleaned_data['songID'] <0 ))):
			print "Enter positive"
			return HttpResponseRedirect(reverse_lazy('songappears_list'))
		print "FORM VALID"
		#print self
		self.object = form.save(commit=False)

		#print form.cleaned_data
		Performs.objects.filter(songID=self.object).delete()
		for performer in form.cleaned_data['performs']:
			print performer
			print type(performer)
			print "\n\n\n\n"
			print "OBJECT"
			print self.object
			print type(self.object)
			performance = Performs()
			performance.songID = self.object
			performance.ssn = performer
			self.object.save() #THIS IS WORKING NOW
			performance.save()
			#form.save_m2m()
		return super(ModelFormMixin,self).form_valid(form)
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('songappears_list'))

		return super(SongAppearsUpdate, self).post(request, *args, **kwargs)

class SongAppearsDelete(LoginRequiredMixin,DeleteView):
	model = SongAppears
	success_url = reverse_lazy('songappears_list')
	fields = '__all__'
	login_url = '/notownapp/login/'



	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('songappears_list'))

		return super(SongAppearsDelete, self).post(request, *args, **kwargs)

class SongAppearsCreate(LoginRequiredMixin,CreateView):
	model = SongAppears
	success_url = reverse_lazy('songappears_list')
	fields = '__all__'
	login_url = '/notownapp/login/'

	def form_valid(self,form):
		print "FORM VALID"
		#print self
		self.object = form.save(commit=False)

		if(((form.cleaned_data['songID'] <0 ))):
			print "Enter positive"
			return HttpResponseRedirect(reverse_lazy('songappears_list'))

		print form.cleaned_data
		for performer in form.cleaned_data['performs']:
			print performer
			print type(performer)
			print "\n\n\n\n"
			print "OBJECT"
			print self.object
			print type(self.object)
			performance = Performs()
			performance.songID = self.object
			performance.ssn = performer
			self.object.save() #THIS IS WORKING NOW
			performance.save()
			#form.save_m2m()

		return super(ModelFormMixin,self).form_valid(form)
	def post(self, request, *args, **kwargs):
		print "USER"
		print self.request.user
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('songappears_list'))

		return super(SongAppearsCreate, self).post(request, *args, **kwargs)


class PerformsCreate(LoginRequiredMixin,CreateView):
	model = Performs
	success_url = reverse_lazy('performs_list')
	fields = '__all__'
	login_url = '/notownapp/login/'

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('performs_list'))

		return super(PerformsCreate, self).post(request, *args, **kwargs)



class PerformsList(LoginRequiredMixin,ListView):
	model = Performs
	context_object_name = 'performs'
	success_url = reverse_lazy('performs_list')
	fields = '__all__'
	login_url = '/notownapp/login/'

	def get_queryset(self):
		print "Performs Queryset"

		SONGID= self.request.GET.get("songID")
		SSN = self.request.GET.get("ssn")

		#Performs.objects.all()
		#Performs.objects.filter(ssn__ssn__icontains="")
		#Performs.objects.filter(songID__songID__icontains="")

		if SONGID is not None and SSN is not None:
			queryset=Performs.objects.filter(songID__songID__icontains=SONGID)
			print queryset
			queryset = queryset.filter(ssn__ssn__icontains=SSN)
			print queryset
			return queryset
		else:
			return Performs.objects.all()


class PerformsUpdate(LoginRequiredMixin,UpdateView):
	model = Performs
	success_url = reverse_lazy('performs_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def get_object(self):
		print self.kwargs
		SONGID,SSN = self.kwargs['pk'].split("p")
		print SSN,SONGID
		return Performs.objects.get(songID=SONGID,ssn=SSN)

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('performs_list'))

		return super(PerformsUpdate, self).post(request, *args, **kwargs)

class PerformsDelete(LoginRequiredMixin,DeleteView):
	model = Performs
	success_url = reverse_lazy('performs_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	#return str(self.songID.songID) + "p"  + str(self.ssn.ssn)
	def get_object(self):
		print self.kwargs
		SONGID,SSN = self.kwargs['pk'].split("p")
		print SSN,SONGID
		return Performs.objects.get(songID=SONGID,ssn=SSN)

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('performs_list'))

		return super(PerformsDelete, self).post(request, *args, **kwargs)

class PlacesList(LoginRequiredMixin,ListView):
	model = Places
	context_object_name = 'places'
	success_url = reverse_lazy('places_list')
	fields = '__all__'
	login_url = '/notownapp/login/'

	#Places.objects.filter(address__icontains="STRING")
	def get_queryset(self):
		print "Places Queryset"

		ADDRESS= self.request.GET.get("address")

		if ADDRESS is not None:
			queryset=Places.objects.filter(address__icontains=ADDRESS)
			return queryset
		else:
			return Places.objects.all()


class PlacesCreate(LoginRequiredMixin,CreateView):
	model = Places
	success_url = reverse_lazy('places_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	print "CREATE PLACE"
	def form_valid(self,form):
		print form
		print form.cleaned_data['address']
		return super(PlacesCreate, self).form_valid(form)

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('places_list'))

		return super(PlacesCreate, self).post(request, *args, **kwargs)



	#	return super(PlacesCreate, self).post(request, *args, **kwargs)



class PlacesUpdate(LoginRequiredMixin,UpdateView):
	model = Places
	success_url = reverse_lazy('places_list')
	fields = '__all__'
	login_url = '/notownapp/login/'

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('places_list'))

		return super(PlacesUpdate, self).post(request, *args, **kwargs)

class PlacesDelete(LoginRequiredMixin,DeleteView):
	model = Places
	success_url = reverse_lazy('places_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('places_list'))

		return super(PlacesDelete, self).post(request, *args, **kwargs)

class Telephone_HomeList(LoginRequiredMixin,ListView):
	model = Telephone_Home
	context_object_name = 'telephonehomes'
	success_url = reverse_lazy('telephone_homes_list')
	fields = '__all__'
	login_url = '/notownapp/login/'


	def get_queryset(self):
		print "Telephone Queryset"

		PHONE= self.request.GET.get("phone")
		ADDRESS = self.request.GET.get("address")
		#Telephone_Home.objects.filter(phone__icontains="85")
		#Telephone_Home.objects.filter(address__address__icontains="85")

		if PHONE is not None and ADDRESS is not None:
			queryset=Telephone_Home.objects.filter(phone__icontains=PHONE)
			print queryset
			queryset = queryset.filter(address__address__icontains=ADDRESS)
			print queryset
			return queryset
		else:
			return Telephone_Home.objects.all()


class Telephone_HomeCreate(LoginRequiredMixin,CreateView):
	model = Telephone_Home
	#context_object_name = 'telephonehomes'
	success_url = reverse_lazy('telephone_homes_list')
	fields = '__all__'
	login_url = '/notownapp/login/'

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('telephone_homes_list'))

		return super(Telephone_HomeCreate, self).post(request, *args, **kwargs)

class Telephone_HomeUpdate(LoginRequiredMixin,UpdateView):
	model = Telephone_Home
	#context_object_name = 'telephonehomes'
	success_url = reverse_lazy('telephone_homes_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('telephone_homes_list'))

		return super(Telephone_HomeUpdate, self).post(request, *args, **kwargs)

class Telephone_HomeDelete(LoginRequiredMixin,DeleteView):
	model = Telephone_Home
	#context_object_name = 'telephonehomes'
	success_url = reverse_lazy('telephone_homes_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('telephone_homes_list'))

		return super(Telephone_HomeDelete, self).post(request, *args, **kwargs)


class LivesList(LoginRequiredMixin,ListView):
	model = Lives
	context_object_name='lives'
	success_url = reverse_lazy('lives_list')
	fields = '__all__'
	login_url = '/notownapp/login/'

	def get_queryset(self):
		print "Lives Queryset"

		SSN= self.request.GET.get("ssn")
		PHONE = self.request.GET.get("phone")
		ADDRESS = self.request.GET.get("address")
		#Lives.objects.filter(ssn__ssn__icontains=85)
		#Lives.objects.filter(phone__phone__icontains=85)
		#Lives.objects.filter(address__address__icontains=85)

		if SSN is not None and PHONE is not None and ADDRESS is not None:
			print "IN NOT NONE"
			queryset=Lives.objects.filter(phone__phone__icontains=PHONE)
			print queryset
			queryset = queryset.filter(address__address__icontains=ADDRESS)
			print queryset
			queryset = queryset.filter(ssn__ssn__icontains=SSN)
			print queryset
			return queryset
		else:
			return Lives.objects.all()


class LivesUpdate(LoginRequiredMixin,UpdateView):
	model = Lives
	#context_object_name='lives'
	success_url = reverse_lazy('lives_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('lives_list'))

		return super(LivesUpdate, self).post(request, *args, **kwargs)

	def get_object(self):
		print self.kwargs
		SSN,ADDRESS = self.kwargs['pk'].split("L")
		print SSN,ADDRESS
		return Lives.objects.get(ssn=SSN,address=ADDRESS)

class LivesDelete(LoginRequiredMixin,DeleteView):
	model = Lives
	#context_object_name='lives'
	success_url = reverse_lazy('lives_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def get_object(self):
		print self.kwargs
		SSN,ADDRESS = self.kwargs['pk'].split("L")
		print SSN,ADDRESS
		return Lives.objects.get(ssn=SSN,address=ADDRESS)

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('lives_list'))

		return super(LivesDelete, self).post(request, *args, **kwargs)

class LivesCreate(LoginRequiredMixin,CreateView):
	model = Lives
	#context_object_name='lives'
	success_url = reverse_lazy('lives_list')
	fields = '__all__'
	login_url = '/notownapp/login/'
	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430@SIUC":
			return HttpResponseRedirect(reverse_lazy('lives_list'))

		return super(LivesCreate, self).post(request, *args, **kwargs)
