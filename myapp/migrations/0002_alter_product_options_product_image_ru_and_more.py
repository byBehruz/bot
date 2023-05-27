# Generated by Django 4.2 on 2023-05-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='image_ru',
            field=models.ImageField(blank=True, help_text='Upload Image', null=True, upload_to='media/', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_uz',
            field=models.ImageField(blank=True, help_text='Upload Image', null=True, upload_to='media/', verbose_name='Image'),
        ),
        migrations.AlterModelTable(
            name='botuser',
            table=None,
        ),
    ]