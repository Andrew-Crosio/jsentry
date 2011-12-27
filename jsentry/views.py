from django.http import HttpResponse
from sentry.client.models import client
import logging

def js_error_handler(request, *args, **kwargs):

    message = request.POST.get('message', None)
    url = request.POST.get('url', None)

    client.create_from_text(message, level=logging.ERROR, url=url, request=request)
    return HttpResponse('true')
