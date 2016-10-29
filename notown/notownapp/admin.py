from django.contrib import admin

# Register your models here.
from django.apps import apps
from .models import *
#from models import *
#from notownapp.models import models


print "HELLO from admin.py"
#print models


class MembershipInline(admin.TabularInline):
    model=Plays
    extra = 1

class InstrumentsAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

class MusiciansAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

admin.site.register(Musicians,MusiciansAdmin)
admin.site.register(Instruments, InstrumentsAdmin)

app = apps.get_app_config('notownapp')
for model_name,model in app.models.items():
    print model,model_name
    if ('musicians' not in model_name and 'instruments' not in model_name):
        print model
        #print "NOT THE ONES REGISTERED ALREADY"
        admin.site.register(model)
        print "REGISTERED " + str(model)
        #admin.site.register(model)
