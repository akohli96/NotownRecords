from django.conf.urls import url

from . import views
from notownapp.views import *

urlpatterns = [ url(r'^$' , views.index, name='index'),
                url(r'^musicians/$',MusiciansList.as_view(),name='musicians_list'),
                url(r'^musiciansnew/$',MusiciansCreate.as_view(),name='musicians_new'),
                url(r'^musiciansedit/(?P<pk>\d+)$',MusiciansUpdate.as_view(),name='musicians_edit'),
                url(r'^musiciansdelete/(?P<pk>\d+)$',MusiciansDelete.as_view(),name='musicians_delete'),
                url(r'^plays/$',PlaysList.as_view(),name='plays_list'),
                url(r'^playsnew/$',PlaysCreate.as_view(),name='plays_new'),
                url(r'^playsedit/(?P<pk>\d+P\d+)$',PlaysUpdate.as_view(),name='plays_edit'),
                url(r'^plays/(?P<pk>\d+P\d+)$',PlaysDelete.as_view(),name='plays_delete'),
                url(r'^albumproducers/$',Album_ProducerList.as_view(),name="album_producers_list"),
                url(r'^albumproducersnew/$',Album_ProducerCreate.as_view(),name='album_producers_new'),
                url(r'^albumproducersedit/(?P<pk>\d+)$',Album_ProducerUpdate.as_view(),name='album_producers_edit'),
                url(r'^albumproducersdelete/(?P<pk>\d+)$',Album_ProducerDelete.as_view(),name='album_producers_delete'),

               ]

#url(r'^form_test/$', views.form_test,name='form_test')
