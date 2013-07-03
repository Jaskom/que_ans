from django.conf.urls import patterns, include, url
from que_ans_app.views import addQuestion
from que_ans_app.views import listQuestions
from que_ans_app.views import queryById
from que_ans_app.views import index
from que_ans_app.views import saveAanswer
from que_ans_app.views import preregister
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'que_ans.views.home', name='home'),
    # url(r'^que_ans/', include('que_ans.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^add/$', addQuestion),
    url(r'^list/$', listQuestions),
    url(r'^preregister/$', preregister),
    url(r'^query/$', queryById),
    url(r'^saveAns/$', saveAanswer),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/dgproject/que_ans/static'}
    ),

)
