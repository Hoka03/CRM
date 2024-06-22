from django.shortcuts import redirect
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),


    path("__debug__/", include("debug_toolbar.urls")),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('apps.users.urls')),
    path('attendances/', include('apps.attendances.urls')),
    path('exams/', include('apps.exams.urls')),
    # path('general/', include('apps.general.urls')),
    path('groups/', include('apps.groups.urls')),
    path('lessons/', include('apps.lessons.urls')),
    path('notices/', include('apps.notices.urls')),
    path('payments/', include('apps.payments.urls')),
    path('subjects/', include('apps.subjects.urls'))
)