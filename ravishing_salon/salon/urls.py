from django.conf.urls import url

from . import views
#app_name = 'searchengine'
urlpatterns = [

    url(r'^$', views.index, name='index'),
 	url(r'^(?P<id>[0-9]+)/$',views.salonDetails, name='details'),
 	url(r'^upload/$',views.upload_form, name='upload_form'),
 	#url(r'^(?P<id>[0-9]+)/imageupload',views.uploadImages, name='imageupload'),
 	url(r'^(?P<id>[0-9]+)/gallery',views.gallery, name='gallery'),

    ]
