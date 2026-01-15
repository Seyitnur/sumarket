from modeltranslation.translator import register, TranslationOptions
from products.models import *

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
