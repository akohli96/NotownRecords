from django.db import models


class Musicians(models.Model):
    name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return str(self.name) + " " + str(self.ssn)

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

class SongAppears(models.Model):
    songID = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    albumident = models.ForeignKey(Album_Producer)
    performs = models.ManyToManyField(Musicians,through="Performs")

class Performs(models.Model):
    ssn = models.ForeignKey(Musicians)
    songID = models.ForeignKey(SongAppears,related_name="songid")

    class Meta:
        unique_together=('ssn','songID')


class Places(models.Model):
    address = models.CharField(max_length=30,primary_key=True)

class Telephone_Home(models.Model):
    phone = models.CharField(max_length=11,primary_key=True)
    address = models.OneToOneField(Places) #should take care of unique

class Lives(models.Model):
    ssn = models.ForeignKey(Musicians)
    phone = models.ForeignKey(Telephone_Home)
    address = models.ForeignKey(Places)

    class Meta:
        unique_together=('ssn','address')
