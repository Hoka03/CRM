from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.subjects.models import Subject, Resource


@admin.register(Subject)
class SubjectAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'price', 'created_at')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name']}
    group_fieldsets = True


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'title', 'confirmed_by', 'url', 'published_at')
    list_display_links = list_display
