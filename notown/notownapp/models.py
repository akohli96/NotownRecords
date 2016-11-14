from django.db import models
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS


class Musicians(models.Model):
    name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return str(self.name) + " " + str(self.ssn)

    def get_absolute_url(self):
        return reverse('musicians-detail', kwargs={'pk': self.ssn})

class Instruments(models.Model):
    instrld = models.CharField(max_length=10,primary_key=True)
    dname = models.CharField(max_length=30)
    key = models.CharField(max_length=5)
    plays = models.ManyToManyField(Musicians,through='Plays')

    def __str__(self):
        return str(self.instrld) + " " + str(self.dname) + " " +  str(self.key) + " " + str(self.plays)

#Using through table
class Plays (models.Model):
    ssn = models.ForeignKey(Musicians)
    instrld = models.ForeignKey(Instruments,related_name="playdata")

    class Meta:
        unique_together = ('ssn','instrld')

    def __str__(self):
        return str(self.ssn) + " " + str(self.instrld)


class Album_Producer(models.Model):
    albumident = models.IntegerField(primary_key=True,default=-1)
    ssn = models.ForeignKey(Musicians)
    copyright = models.DateField()
    speed = models.IntegerField()
    title = models.CharField(max_length=30)

    def __str__(self):
        return str(self.albumident) + " " + str(self.ssn) +" " +  str(self.copyright) + " " + str(self.speed) + " " + str(self.title)

"""
This has to be searched by customers. Input can be title,author or the Album_Producer title

"""

#Filter can also be applied
#SongAppears.objects.get(title__contains="Song1")
#SongAppears.objects.get(author__contains="Ayush")
#SongAppears.objects.get(albumident__title="Ayush Album1")
class SongAppears(models.Model):
    songID = models.IntegerField(primary_key=True)
    author = models.ForeignKey(Musicians,related_name="musicianname")
    title = models.CharField(max_length=30)
    albumident = models.ForeignKey(Album_Producer)
    performs = models.ManyToManyField(Musicians,through="Performs")

    def __str__(self):
        return str(self.songID) + " \n " + str(self.author) + " \n " + str(self.title) + " \n " + str(self.albumident) + " \n " + str(self.performs)

    #def clean(self):
        #if(self.performs is None):
        #    raise ValidationError(('Each song must be performed by atleast one musician.Add to performance'))
        if(self.author != self.albumident.ssn):
            raise ValidationError(('The song author and album author must be the same musician'))

    def save(self):
        try:
            self.full_clean()
        except ValidationError as e:
            print e

class Performs(models.Model):
    ssn = models.ForeignKey(Musicians)
    songID = models.ForeignKey(SongAppears,related_name="songid")

    class Meta:
        unique_together=('ssn','songID')

    def __str__(self):
        return str(self.ssn) + " " + str(self.songID)


class Places(models.Model):
    address = models.CharField(max_length=30,primary_key=True)

    def __str__(self):
        return str(self.address)

class Telephone_Home(models.Model):
    phone = models.CharField(max_length=11,primary_key=True)
    address = models.OneToOneField(Places) #should take care of unique

    def __str__(self):
        return str(self.phone) + " " + str(self.address)

class Lives(models.Model):
    ssn = models.ForeignKey(Musicians)
    phone = models.ForeignKey(Telephone_Home)
    address = models.ForeignKey(Places)

    class Meta:
        unique_together=('ssn','address')

    def __str__(self):
        return str(self.ssn) + " " + str(self.phone) + " " + str(self.address)

    #print str(self.phone)
    def clean(self):
        if (self.address != self.phone.address):
            raise ValidationError(('Phone and address phone need to be the same.'))
    def save(self):
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
