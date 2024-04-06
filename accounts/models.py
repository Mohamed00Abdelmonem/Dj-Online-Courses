from django.db import models
from django.contrib.auth.models import User, Group
from courses.models import Course
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.generate_code import generate_code




class Instructor_Profile(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, default=generate_code)
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Teachers'})
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

# @receiver(post_save, sender=User)
# def ceate_profile(sender, instance, created, **kwargs):
#     if created:
#         Instructor_Profile.objects.create(
#             user=instance
#         )


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        teachers_group, _ = Group.objects.get_or_create(name='Teachers')  # Get or create Students group
        if teachers_group in instance.groups.all():  # Check if user belongs to Students group
            Instructor_Profile.objects.create(user=instance)  # Create a Student_Profile instance for the user




class Student_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Students'})
    code = models.CharField(max_length=10, default=generate_code)
    image = models.ImageField(upload_to='students', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    interests = models.CharField(max_length=200, null=True, blank=True)
    courses_enrolled = models.ManyToManyField('courses.Course', related_name='students', blank=True)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        student_group, _ = Group.objects.get_or_create(name='Students')  # Get or create Students group
        if student_group in instance.groups.all():  # Check if user belongs to Students group
            Student_Profile.objects.create(user=instance)  # Create a Student_Profile instance for the user
