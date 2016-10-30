from django.conf.urls import url

from . import views

urlpatterns = [ url(r'^$' , views.index, name='index'),
               url(r'^form_test/$', views.form_test,name='form_test')
               ]
