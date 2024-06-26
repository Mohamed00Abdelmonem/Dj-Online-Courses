# Generated by Django 5.0.3 on 2024-04-03 00:05

import django_summernote.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='company/logos/')),
                ('carousel_image1', models.ImageField(upload_to='company/carousel/')),
                ('carousel_image2', models.ImageField(upload_to='company/carousel/')),
                ('description', models.TextField()),
                ('about_us', django_summernote.fields.SummernoteTextField()),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('social_media_facebook', models.URLField(blank=True, null=True)),
                ('social_media_whatsapp', models.URLField(blank=True, null=True)),
                ('social_media_youtube', models.URLField(blank=True, null=True)),
                ('social_media_other_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
