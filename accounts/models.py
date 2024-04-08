from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.generate_code import generate_code




class Profile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name='profile_user', on_delete=models.CASCADE)
    code = models.CharField(max_length=10, default=generate_code)
    image = models.ImageField(upload_to='instructors', null=True, blank=True)
    sub_descriptions = models.TextField(null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    experiences = models.TextField(null=True, blank=True)
    skill_level = models.CharField(max_length=100, null=True, blank=True)
    language_use = models.CharField(max_length=100, null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name='instructors', blank=True)
    about_for_instructor = models.TextField(null=True, blank=True)
    social_media_facebook = models.URLField(max_length=200, null=True, blank=True)
    social_media_twitter = models.URLField(max_length=200, null=True, blank=True)
    social_media_youtube = models.URLField(max_length=200, null=True, blank=True)
    social_media_instagram = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return (f"{self.user}")

@receiver(post_save, sender=User)
def ceate_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )



