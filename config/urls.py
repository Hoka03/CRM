from django.shortcuts import redirect
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


def set_language(request):
    language_code = request.POST.get('language', 'en')
    redirect_url = request.POST.get('next', '/')
    return redirect(request.META['HTTP_ORIGIN'] + f'/{language_code}/')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('i18n/', include('django.conf.urls.i18n')),
    path('set-lang/', set_language, name='set_language'),
    path('i18n/', include('django.conf.urls.i18n')),

    path("__debug__/", include("debug_toolbar.urls")),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('apps.subjects.urls')),

)