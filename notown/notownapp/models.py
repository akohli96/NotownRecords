from django.db import models


class Musicians(models.Model):
    name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=10, primary_key=True)

class Instruments(models.Model):
    instrld = models.CharField(max_length=10,primary_key=True)
    dname = models.CharField(max_length=30)
    key = models.CharField(max_length=5)
    plays = models.ManyToManyField(Musicians,through='Membership')

#Using through table
class Membership (models.Model):
    ssn = models.ForeignKey(Musicians)
    instrld = models.ForeignKey(Instruments)

    class Meta:
        unique_together = ('ssn','instrld')


class SongAppears(models.Model):
    songID = models.IntegerField()

class Telephone_Home(models.Model):
    phone = models.CharField(max_length=11,primary_key=True)
    address = models.ForeignKey('Places') #since not defined yet


class Places(models.Model):
    address = models.CharField(max_length=30,primary_key=True)
    #address = models.ForeignKey(Telephone_Home)

#class Lives(models.Model):
