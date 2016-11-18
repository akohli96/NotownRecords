from django.db import models
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.core.urlresolvers import reverse


class Musicians(models.Model):
    name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return str(self.name) + " " + str(self.ssn)

    def get_absolute_url(self):
        return reverse('musicians-detail', kwargs={'pk': self.ssn})

#Instruments.objects.filter(instrld__icontains="")
#Instruments.objects.filter(dname__icontains="")
#Instruments.objects.filter(keys__icontains="")
#Instruments.objects.filter(instrld__icontains="")
#Instruments.objects.filter(plays__ssn__icontains="")
#Instruments.objects.filter(plays__instrld__icontains="")
class Instruments(models.Model):
    instrld = models.CharField(max_length=10,primary_key=True)
    dname = models.CharField(max_length=30)
    key = models.CharField(max_length=5)
    plays = models.ManyToManyField(Musicians,through='Plays')

    def __str__(self):
        return str(self.instrld) + " " + str(self.dname) + " " +  str(self.key) + " " + str(self.plays)

    def get_absolute_url(self):
        return reverse('instruments-detail', kwargs={'pk': self.instrld})
    """
    >>> for musician in i2.plays.all():
    ...  print musician
    ...
    Bob 8532531563
    >>> Instruments.objects.get(pk=2)
    <Instruments: 2 G-G Bflat notownapp.Musicians.None>
    >>>http://stackoverflow.com/questions/387686/what-are-the-steps-to-make-a-modelform-work-with-a-manytomany-relationship-with

    """

#Using through table
#Plays.objects.filter(ssn__ssn__icontains="")
#Plays.objects.filter(instrld__instrld__icontains="")
class Plays (models.Model):
    ssn = models.ForeignKey(Musicians)
    instrld = models.ForeignKey(Instruments,related_name='plays_instrld_instruments')

    class Meta:
        unique_together = ('ssn','instrld')

    def __str__(self):
        return str(self.ssn.ssn) + " " +  str(self.instrld.instrld)

    def urlify(self):
        return str(self.ssn.ssn) + "P"  + str(self.instrld.instrld)

    def get_absolute_url(self):
        return reverse('plays-detail', kwargs={'pk': urlify(self)})


#queryset = Album_Producer.objects.filter(albumident__icontains=ALBUMIDENTIFIER)
#queryset = queryset.filter(copyright__icontains=COPYRIGHTDATE)
#queryset = queryset.filter(title__icontains=TITLE)
#queryset = queryset.filter(speed__icontains=SPEED)
#queryset = queryset.filter(ssn__ssn__icontains=SSN)
class Album_Producer(models.Model):
    albumident = models.IntegerField(primary_key=True,default=-1)
    ssn = models.ForeignKey(Musicians)
    copyright = models.DateField()
    speed = models.IntegerField()
    title = models.CharField(max_length=30)

    def __str__(self):
        return str(self.albumident) + " " + str(self.ssn) +" " +  str(self.copyright) + " " + str(self.speed) + " " + str(self.title)


    def get_absolute_url(self):
        return reverse('album_producer-detail',kwargs={'pk' : self.albumident})

"""
This has to be searched by customers. Input can be title,author or the Album_Producer title

"""

#Filter can also be applied
#SongAppears.objects.get(title__contains="Song1")
#SongAppears.objects.get(author__contains="Ayush")
#SongAppears.objects.get(albumident__title="Ayush Album1")
#https://docs.djangoproject.com/en/1.10/topics/db/examples/many_to_many/
#SongAppears.objects.filter(performs__ssn__icontains=853253156)
#SongAppears.objects.filter(albumident=1)
#SongAppears.objects.filter(albumident__albumident__icontains=1)
#SongAppears.objects.filter(albumident__title__icontains="AY")
class SongAppears(models.Model):
    songID = models.IntegerField(primary_key=True)
    author = models.ForeignKey(Musicians,related_name="song_author_musicians")
    title = models.CharField(max_length=30)
    albumident = models.ForeignKey(Album_Producer)
    performs = models.ManyToManyField(Musicians,through="Performs")

    def __str__(self):
        return str(self.songID) + " \n " + str(self.author) + " \n " + str(self.title) + " \n " + str(self.albumident) + " \n " + str(self.performs)


    def clean(self):
        if(self.performs is None):
            raise ValidationError(('Each song must be performed by atleast one musician.Add to performance'))
        #if(self.author != self.albumident.ssn):
        #    raise ValidationError(('The song author and album author must be the same musician'))

    def save(self, *args, **kwargs):
        try:
            self.full_clean()
        except ValidationError as e:
            print e

    def get_absolute_url(self):
        return reverse('songappears-detail',kwargs={'pk' : self.songID})


#Performs.objects.all()
#Performs.objects.filter(ssn__ssn__icontains="")
#Performs.objects.filter(songID__songID__icontains="")
class Performs(models.Model):
    ssn = models.ForeignKey(Musicians)
    songID = models.ForeignKey(SongAppears,related_name="perform_songID_song")

    class Meta:
        unique_together=('ssn','songID')

    def __str__(self):
        return str(self.ssn) + " " + str(self.songID)

    def urlify(self):
        return str(self.songID.songID) + "p"  + str(self.ssn.ssn)

    def get_absolute_url(self):
        return reverse('performs-detail', kwargs={'pk': urlify(self)})

#Places.objects.filter(address__icontains="STRING")
class Places(models.Model):
    address = models.CharField(max_length=30,primary_key=True)

    def __str__(self):
        return str(self.address)

    def get_absolute_url(self):
        return reverse('address-detail', kwargs={'pk' : self.address})

#Telephone_Home.objects.filter(phone__icontains="85")
#Telephone_Home.objects.filter(address__address__icontains="85")
class Telephone_Home(models.Model):
    phone = models.CharField(max_length=11,primary_key=True)
    address = models.OneToOneField(Places) #should take care of unique

    def __str__(self):
        return str(self.phone) + " " + str(self.address)

    def get_absolute_url(self):
        return reverse('telephone_home-detail', kwargs={'pk' : self.phone})

#Lives.objects.filter(ssn__ssn__icontains=85)
#Lives.objects.filter(phone__phone__icontains=85)
#Lives.objects.filter(address__address__icontains=85)
class Lives(models.Model):
    ssn = models.ForeignKey(Musicians)
    phone = models.ForeignKey(Telephone_Home)
    address = models.ForeignKey(Places)

    class Meta:
        unique_together=('ssn','address')

    def __str__(self):
        return str(self.ssn) + " " + str(self.phone) + " " + str(self.address)

    def urlify(self):
        return str(self.ssn.ssn) + "LIVES" + str(self.address.address)

    def get_absolute_url(self):
        return reverse('lives-detail', kwargs={'pk' : urlify(self)})



    #print str(self.phone)
    def clean(self):
        if (self.address != self.phone.address):
            raise ValidationError(('Phone and address phone need to be the same.'))
    def save(self, *args, **kwargs):
        try:
            self.full_clean()
        except ValidationError as e:
            print e

#https://docs.djangoproject.com/en/1.10/topics/db/queries/
#https://docs.djangoproject.com/en/1.10/ref/forms/fields/

"""
Customers can search for records by name of the musician, title of the album, and
name of the song.
b. Notown staff can search any table and can add/delete/alter a row in any table. Each
Notown staff member has to provide this security code, cs430@SIUC, before she/he
can submit an update command. No security check is needed for pure search.

"""
