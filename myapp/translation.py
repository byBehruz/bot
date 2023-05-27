from .models import *
from modeltranslation.translator import register, TranslationOptions



@register(Product)
class ProductTRaanslationOptions(TranslationOptions):
    fields=('name', 'about', 'image')

# @register(Category)
# class CategoryTRanslationOptions(TranslationOptions):
#     fields = ('name')