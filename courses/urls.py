from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.course_list),
    url(r'^courses/$', views.course_list),
    url(r'^courses/new/$', views.course_new, name='course_new'),
    url(r'^courses/(?P<pk>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^courses/(?P<pk>[0-9]+)/edit/$', views.course_edit, name='course_edit'),
    url(r'^courses/(?P<pk>[0-9]+)/register/(?P<upk>[0-9]+)$', views.course_register, name='course_register'),
    url(r'^courses/(?P<pk>[0-9]+)/deregister/(?P<upk>[0-9]+)$', views.course_deregister, name='course_deregister'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^accounts/', include('django.contrib.auth.urls')),

)
