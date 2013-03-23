from django.conf.urls import patterns, include, url

from .views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^microblog/', include('microblog.foo.urls')),
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'),

)
