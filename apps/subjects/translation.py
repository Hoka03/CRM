from modeltranslation.translator import TranslationOptions, register

from apps.subjects.models import Subject


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('name',)