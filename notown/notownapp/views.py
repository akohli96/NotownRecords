from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms import forms
from notownapp.forms import *

import re

def index(request):
	return HttpResponse("WELCOME TO Notown App")

"""
def form_test(request):
	mform = SongAppearsForm()
	return render(request,'notownapp/form_test.html',{'MusiciansForm': mform})

#def search_normal(re)
"""


class Album_ProducerList(ListView):
	model = Album_Producer
	context_object_name = 'album_producers'


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



class Album_ProducerCreate(CreateView):
	model = Album_Producer
	success_url = "/notownapp/albumproducerslist/"
	fields = "__all__"

class Album_ProducerUpdate(UpdateView):
	model = Album_Producer
	success_url = reverse_lazy('album_producers_list')
	#context_object_name = 'musicians'
	fields = '__all__'

class Album_ProducerDelete(DeleteView):
	model = Album_Producer
	success_url = reverse_lazy('album_producers_list')
	#context_object_name = 'musicians'
	fields = '__all__'

	def post(self, request, *args, **kwargs):
		print request.POST
		print request.POST["password"]
		if request.POST["password"] != "cs430":
			return HttpResponseRedirect(reverse_lazy('album_producers_list'))

		return super(Album_ProducerDelete, self).post(request, *args, **kwargs)

class MusiciansList(ListView):
	model = Musicians
	context_object_name = 'musicians'
	#Musicians.objects.filter(ssn__contains=853253156,name__contains="Ayush")
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

class InstrumentsList(ListView):
	model = Instruments
	context_object_name = 'instruments'
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


class InstrumentsCreate(CreateView):
	model = Instruments
	success_url = reverse_lazy('instruments_list')
	fields = '__all__'

class InstrumentsUpdate(UpdateView):
	model = Instruments
	success_url = reverse_lazy('instruments_list')
	fields = '__all__'

class InstrumentsDelete(DeleteView):
	model = Instruments
	success_url = reverse_lazy('instruments_list')
	fields = '__all__'

class SongAppearsList(ListView):
	model = SongAppears
	context_object_name = 'songappears'
	success_url = reverse_lazy('songappears_list')
	fields = '__all__'

	def get_queryset(self):
		print "SongAppears Queryset"

		SONGID= self.request.GET.get("songID")
		AUTHOR = self.request.GET.get("author")
		TITLE = self.request.GET.get("title")
		ALBUMIDENT = self.request.GET.get("albumident")
		PERFORMS = self.request.GET.get("performs")
		#print INSTRLD,DNAME,KEY,PLAYS

		#SongAppears.objects.filter(performs__ssn__icontains=853253156)
		#SongAppears.objects.filter(albumident=1)
		#SongAppears.objects.filter(albumident__albumident__icontains=1)
		#SongAppears.objects.filter(albumident__title__icontains="AY")
		#SongAppears.objects.filter(author__ssn__icontains=8)
		#SongAppears.objects.filter(performs__ssn__icontains=8)

		if SONGID is not None and AUTHOR is not None and TITLE is not None and ALBUMIDENT is not None and PERFORMS is not None:
			queryset=SongAppears.objects.filter(songID__icontains=SONGID)
			print queryset
			queryset = queryset.filter(author__ssn__icontains=AUTHOR)
			print queryset
			queryset = queryset.objects.filter(albumident__albumident__icontains=ALBUMIDENT)
			print queryset
			queryset = queryset.objects.filter(performs__ssn__icontains=PERFORMS)
			return queryset
		else:
			return SongAppears.objects.all()

class SongAppearsUpdate(UpdateView):
	model = SongAppears
	success_url = reverse_lazy('songappears_list')
	fields = '__all__'

class SongAppearsDelete(DeleteView):
	model = SongAppears
	success_url = reverse_lazy('songappears_list')
	fields = '__all__'

class SongAppearsCreate(CreateView):
	model = SongAppears
	success_url = reverse_lazy('songappears_list')
	fields = '__all__'


class PerformsCreate(CreateView):
	model = Performs
	success_url = reverse_lazy('performs_list')
	fields = '__all__'

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

class PerformsList(ListView):
	model = Performs
	context_object_name = 'performs'
	success_url = reverse_lazy('performs_list')
	fields = '__all__'

	#Performs.objects.filter(ssn__ssn__icontains="")
	#Performs.objects.filter(songID__songID__icontains="")



class PerformsUpdate(UpdateView):
	model = Performs
	success_url = reverse_lazy('performs_list')
	fields = '__all__'
	def get_object(self):
		print self.kwargs
		SONGID,SSN = self.kwargs['pk'].split("p")
		print SSN,SONGID
		return Performs.objects.get(songID=SONGID,ssn=SSN)

class PerformsDelete(DeleteView):
	model = Performs
	success_url = reverse_lazy('performs_list')
	fields = '__all__'
	#return str(self.songID.songID) + "p"  + str(self.ssn.ssn)
	def get_object(self):
		print self.kwargs
		SONGID,SSN = self.kwargs['pk'].split("p")
		print SSN,SONGID
		return Performs.objects.get(songID=SONGID,ssn=SSN)

class PlacesList(ListView):
	model = Places
	context_object_name = 'places'
	success_url = reverse_lazy('places_list')
	fields = '__all__'

	#Places.objects.filter(address__icontains="STRING")
	def get_queryset(self):
		print "Places Queryset"

		ADDRESS= self.request.GET.get("address")

		if ADDRESS is not None:
			queryset=Places.objects.filter(address__icontains=ADDRESS)
			return queryset
		else:
			return Places.objects.all()


class PlacesCreate(CreateView):
	model = Places
	success_url = reverse_lazy('places_list')
	fields = '__all__'
	print "CREATE PLACE"
	def form_valid(self,form):
		print form
		print form.cleaned_data['address']
		return super(PlacesCreate, self).form_valid(form)

	def post(self, request, *args, **kwargs):
		#print request.args
		print request.POST['address']
		#print #request.POST["password"]
		#if request.POST["password"] != "cs430":
		#	return HttpResponseRedirect(reverse_lazy('plays_list'))



		return super(PlacesCreate, self).post(request, *args, **kwargs)



class PlacesUpdate(UpdateView):
	model = Places
	success_url = reverse_lazy('places_list')
	fields = '__all__'

class PlacesDelete(DeleteView):
	model = Places
	success_url = reverse_lazy('places_list')
	fields = '__all__'

class Telephone_HomeList(ListView):
	model = Telephone_Home
	context_object_name = 'telephonehomes'
	success_url = reverse_lazy('telephone_homes_list')
	fields = '__all__'


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


class Telephone_HomeCreate(CreateView):
	model = Telephone_Home
	#context_object_name = 'telephonehomes'
	success_url = reverse_lazy('telephone_homes_list')
	fields = '__all__'

class Telephone_HomeUpdate(UpdateView):
	model = Telephone_Home
	#context_object_name = 'telephonehomes'
	success_url = reverse_lazy('telephone_homes_list')
	fields = '__all__'

class Telephone_HomeDelete(DeleteView):
	model = Telephone_Home
	#context_object_name = 'telephonehomes'
	success_url = reverse_lazy('telephone_homes_list')
	fields = '__all__'


class LivesList(ListView):
	model = Lives
	context_object_name='lives'
	success_url = reverse_lazy('lives_list')
	fields = '__all__'


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


class LivesUpdate(UpdateView):
	model = Lives
	#context_object_name='lives'
	success_url = reverse_lazy('lives_list')
	fields = '__all__'

	def get_object(self):
		print self.kwargs
		SSN,ADDRESS = self.kwargs['pk'].split("LIVES")
		print SSN,ADDRESS
		return Lives.objects.get(ssn=SSN,address=ADDRESS)

class LivesDelete(DeleteView):
	model = Lives
	#context_object_name='lives'
	success_url = reverse_lazy('lives_list')
	fields = '__all__'
	def get_object(self):
		print self.kwargs
		SSN,ADDRESS = self.kwargs['pk'].split("LIVES")
		print SSN,ADDRESS
		return Lives.objects.get(ssn=SSN,address=ADDRESS)

class LivesCreate(CreateView):
	model = Lives
	#context_object_name='lives'
	success_url = reverse_lazy('lives_list')
	fields = '__all__'
