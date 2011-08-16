jSentry
=======

jSentry is a pluggable Django application to log clientisde 
Javascript errors in realtime via Django Sentry.

Author: Stephen Diehl ( stephen.m.diehl@gmail.com )

Directions:
===========

1. Install Django Sentry as usual.
2. Add jSentry and Sentry to your `INSTALLED_APPS`

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',

        'sentry',
        'sentry.client',
        'jsentry',
        ...
    )

3. Call `handleErrors('/js_error_handler')` somewhere on your page.

License:
========

Released under a MIT License.
