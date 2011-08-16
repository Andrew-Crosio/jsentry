jSentry
=======

jSentry is a pluggable Django application to log clientisde 
Javascript errors in realtime via Django Sentry.

Author: Stephen Diehl ( stephen.m.diehl@gmail.com )

Directions:
===========

1. Install Django Sentry as usual
1.  Add jSentry and Sentry to your `INSTALLED_APPS`

 >     INSTALLED_APPS = (
 >        'sentry',
 >        'sentry.client',
 >        'jsentry',
 >        ...
 >      )
 
1. Include the urls in your urls.py: 

 >    urlpatterns += url(r'^', include('jsentry.urls'))

1. Call `handleErrors('/js_error_handler/')` somewhere on your page.


License:
========

Released under a MIT License.
