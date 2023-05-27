from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class BotUser(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name', help_text='Enter name', null=True, blank=True)
    telegram_id = models.CharField(max_length=30, verbose_name='Telegram ID', help_text='Enter telegram ID', unique=True)
    language = models.CharField(max_length=4, default='uz', verbose_name='Language', help_text='Enter Language')
    phone = models.CharField(max_length=20,verbose_name='Phone number', help_text='Enter phone number', null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        if self.name:
            return self.name
        else:
            return f"{self.telegram_id} ID foydalanuvchi"
    class Meta:
        verbose_name='BotUser'
        verbose_name_plural='BotUser'

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Category', help_text='Enter category')

    def __str__(self):
        return self.name

from django.utils.html import format_html
class Product(models.Model):
    name=models.CharField(max_length=150, verbose_name='Product', help_text='Enter product name', null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', help_text='Choose category')
    image=models.ImageField(upload_to='media/', verbose_name='Image', help_text='Upload Image',null=True, blank=True)
    about=models.TextField(verbose_name='About', null=True, blank=True)
    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'Mahsulot'
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 120px; height:140px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'фото'

    def str(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Продукты'