from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^js_error_handler/$', 'jsentry.views.js_error_handler'),
)
