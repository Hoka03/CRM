from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def set_language(request, lang):
    next_url = request.META.get("HTTP_REFERER")
    print(next_url)
    response = HttpResponseRedirect(next_url)
    return response
