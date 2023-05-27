from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display=['name','telegram_id','language']
    list_filter = ['language', 'added']
    list_per_page=10
    search_fields=['name', 'language','telegram_id']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']
    list_per_page=10
@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display=['name','image_tag','category']
    search_fields=['name','about','category_name']
    list_per_page= 10
    list_filter=['category']
