from django.conf import settings

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russia'),
    ('uz', 'Uzbek'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'ru', 'uz')

USE_I18N = True

# LOCALE_PATH = [
#     settings.BASER_DIR / 'locale',
# ]