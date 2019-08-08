from modeltranslation.translator import translator, TranslationOptions
from demo_app.models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


translator.register(News, NewsTranslationOptions)
