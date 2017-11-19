from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.course_list),
    url(r'^course/$', views.course_list),

    url(r'^course/new/$', views.course_new, name='course_new'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^course/(?P<pk>[0-9]+)/edit/$', views.course_edit, name='course_edit'),
    url(r'^course/(?P<pk>[0-9]+)/register/(?P<upk>[0-9]+)$', views.course_register, name='course_register'),
    url(r'^course/(?P<pk>[0-9]+)/deregister/(?P<upk>[0-9]+)$', views.course_deregister, name='course_deregister'),
    # url(r'^course/(?P<pk>[0-9]+)/del/$', views.course_del, name='course_del'),

    # url(r'^user/new/$', views.user_new, name='user_new'),
    # url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    # url(r'^user/(?P<pk>[0-9]+)/edit/$', views.user_edit, name='user_edit'),
    # # url(r'^user/(?P<pk>[0-9]+)/del/$', views.user_del, name='user_del'),
    # url(r'^user/$', views.user_list),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    #url(r'^accounts/login/$', login, name='login'),

)
