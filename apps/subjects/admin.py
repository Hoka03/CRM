from django.contrib import admin

from apps.subjects.models import Subject, Resource


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'created_at')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name']}


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'author', 'url', 'published_at')
    list_display_links = list_display
