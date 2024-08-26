from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.aggregates import Avg
from taggit.managers import TaggableManager

# _________________________________________________________________________________________

class Course(models.Model):
    image = models.ImageField(upload_to='course_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_user')
    title = models.CharField(max_length=255)
    rate = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    introduction_video = models.FileField(upload_to='course_videos/', blank=True, null=True)
    duration = models.DurationField(default=0)
    SKILL_LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)
    language = models.CharField(max_length=100)
    certificate = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, max_length=150, null=True, blank=True)


    def avg_rate(self):
        avg = self.reviews.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title

# _________________________________________________________________________________________

class Unit(models.Model):
    title = models.CharField(max_length=40)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="unit_course")
    slug = models.SlugField(unique=True, max_length=150,null=True , blank=True)

    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    
    def __str__(self) -> str:
        return self.title
# _________________________________________________________________________________________



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.message
    

# _________________________________________________________________________________________



class Lesson(models.Model):
    title = models.CharField(max_length=40)
    sub_description = models.TextField(max_length=3000, blank=True, null=True)
    duration = models.DurationField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    # instructor = models.ForeignKey(User, related_name='instructor_lessons', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', related_name="lesson_course", on_delete=models.CASCADE)  # Adjust import to avoid circular import
    unit = models.ForeignKey('courses.Unit', on_delete=models.CASCADE, related_name="lesson_unit")  # Adjust import to avoid circular import
    video = models.FileField(upload_to='lesson_videos/', blank=True, null=True)
    resources = models.FileField(upload_to='lesson_resources/', blank=True, null=True)
    assignment = models.BooleanField(default=False)
    slides = models.FileField(upload_to='lesson_slides/', blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=150, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title} for course {self.course}"


@receiver(post_save, sender=Lesson)
def send_lesson_notification(sender, instance, created, **kwargs):
   if created:
        instructor = instance.instructor
        notification = Notification.objects.create(
            user=instructor,
            message=f"A new lesson '{instance.title}' has been added to the course '{instance.course.title}'."
        )
        send_mail(
            'New Lesson Added',
            render_to_string('email/notification.html', {'notification': notification}),
            'mmohamedabdelm@gmail.com',
            [instructor.email],
            fail_silently=False,
        )

# _________________________________________________________________________________________

class Quiz(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='quiz_unit')
    title = models.CharField(max_length=200)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return f"Quiz for lesson {self.unit}"
    
     

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# _________________________________________________________________________________________


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.text

# _________________________________________________________________________________________


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text
# _________________________________________________________________________________________


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_user")
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.FloatField()
    comment = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.comment[:20]} for course {self.course}"

# _________________________________________________________________________________________


