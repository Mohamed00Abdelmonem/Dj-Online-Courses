from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company/logos/')
    carousel_image1 = models.ImageField(upload_to='company/carousel/')
    carousel_image2 = models.ImageField(upload_to='company/carousel/')
    description = models.TextField()
    about_us = models.TextField()  # Consider using a WYSIWYG editor like Summernote
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    social_media_facebook = models.URLField(blank=True, null=True)
    social_media_whatsapp = models.URLField(blank=True, null=True)
    social_media_youtube = models.URLField(blank=True, null=True)
    social_media_other_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
