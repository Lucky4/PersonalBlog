from django.conf.urls import patterns, url
from PersonalBlog_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^detial/(?P<post_title_slug>[\w\-]+)/$', views.detail, name='detail'),
        url(r'^search_title/(?P<keys>[\w]+)/$', views.search_title, name='search_title'),
        url(r'^search_tag/(?P<tag>[\w]+)/$', views.search_tag, name='search_tag'),
        url(r'^about/$', views.about, name='about'),
)
