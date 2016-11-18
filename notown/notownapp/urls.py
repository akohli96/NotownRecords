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
                url(r'^albumproducerslist/$',Album_ProducerList.as_view(),name="album_producers_list"),
                url(r'^albumproducersnew/$',Album_ProducerCreate.as_view(),name='album_producers_new'),
                url(r'^albumproducersedit/(?P<pk>\d+)$',Album_ProducerUpdate.as_view(),name='album_producers_edit'),
                url(r'^albumproducersdelete/(?P<pk>\d+)$',Album_ProducerDelete.as_view(),name='album_producers_delete'),
                url(r'^instruments/$',InstrumentsList.as_view(),name='instruments_list'),
                url(r'^instrumentsnew/$',InstrumentsCreate.as_view(),name='instruments_new'),
                url(r'^instrumentsedit/(?P<pk>\d+)$',InstrumentsUpdate.as_view(),name='instruments_edit'),
                url(r'^instrumentsdelete/(?P<pk>\d+)$',InstrumentsDelete.as_view(),name='instruments_delete'),
                url(r'^songappears/$',SongAppearsList.as_view(),name='songappears_list'),
                url(r'^songappearsnew/$',SongAppearsCreate.as_view(),name='songappears_new'),
                url(r'^songappearsedit/(?P<pk>\d+)$',SongAppearsUpdate.as_view(),name='songappears_edit'),
                url(r'^songappearsdelete/(?P<pk>\d+)$',SongAppearsDelete.as_view(),name='songappears_delete'),
                url(r'^performs/$',PerformsList.as_view(),name='performs_list'),
                url(r'^performsnew/$',PerformsCreate.as_view(),name='performs_new'),
                url(r'^performsedit/(?P<pk>\d+p\d+)$',PerformsUpdate.as_view(),name='performs_edit'),
                url(r'^performsdelete/(?P<pk>\d+p\d+)$',PerformsDelete.as_view(),name='performs_delete'),
                url(r'^places/$',PlacesList.as_view(),name='places_list'),
                url(r'^placesnew/$',PlacesCreate.as_view(),name='places_new'),
                url(r'^placesedit/(?P<pk>.+)$',PlacesUpdate.as_view(),name='places_edit'),
                url(r'^placesdelete/(?P<pk>.+)$',PlacesDelete.as_view(),name='places_delete'),
                url(r'^telephone/$',Telephone_HomeList.as_view(),name='telephone_homes_list'),
                url(r'^telehpnenew/$',Telephone_HomeCreate.as_view(),name='telephone_homes_new'),
                url(r'^telephoneedit/(?P<pk>\w+)$',Telephone_HomeUpdate.as_view(),name='telephone_homes_edit'),
                url(r'^telephonesdelete/(?P<pk>\w+)$',Telephone_HomeDelete.as_view(),name='telephone_homes_delete'),
                url(r'^lives/$',LivesList.as_view(),name='lives_list'),
                url(r'^livesnew/$',LivesCreate.as_view(),name='lives_new'),
                url(r'^livesedit/(?P<pk>\d+LIVES\w+)$',LivesUpdate.as_view(),name='lives_edit'),
                url(r'^livesdelete/(?P<pk>\d+LIVES\w+)$',LivesDelete.as_view(),name='lives_delete'),


               ]

#url(r'^form_test/$', views.form_test,name='form_test')
