from django.shortcuts import render

from apps.subjects.models import Subject


def home(request):
    subs = Subject.objects.all()
    context = {
        'subs': subs
    }
    return render(request, 'index.html', context)
