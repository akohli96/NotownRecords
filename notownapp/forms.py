from django.forms import ModelForm
from notownapp.models import *

class MusiciansForm(ModelForm):
    class Meta:
        model = Musicians
        fields = '__all__'




class InstrumentsForm(ModelForm):
    class Meta:
        model = Instruments
        fields = '__all__'

class PlaysForm(ModelForm):
    class Meta:
        model = Plays
        fields = '__all__'


class Album_ProducerForm(ModelForm):
    class Meta:
        model = Album_Producer
        fields = '__all__'


"""
THIS IS THE ONE USERS SHOULD ONLY SEE
#Filter can also be applied
#SongAppears.objects.get(title__contains="Song1")
#SongAppears.objects.get(author__contains="Ayush")
#SongAppears.objects.get(albumident__title="Ayush Album1")
"""

class SongAppearsForm(ModelForm):
    class Meta:
        model = SongAppears
        fields = '__all__'
        exclude = ['songID']

    def __init__(self, *args, **kwargs):
        super(SongAppearsForm, self).__init__(*args, **kwargs)
        self.fields['author'].label = 'Musician'
        self.fields['title'].label = 'Song Title'
        self.fields['albumident'].label = 'Song Album'
        self.fields['performs'].label = 'Performances'

class PerformsForm(ModelForm):
    class Meta:
        model = Performs
        fields = '__all__'

class PlacesForm(ModelForm):
    class Meta:
        model = Places
        fields = '__all__'

class Telephone_HomeForm(ModelForm):
    class Meta:
        model = Telephone_Home
        fields = '__all__'

class LivesForm(ModelForm):
    class Meta:
        model = Places
        fields = '__all__'
