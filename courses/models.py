from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg
from taggit.managers import TaggableManager
from django.utils import timezone
from django.utils.text import slugify


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




class Lesson(models.Model):
    title = models.CharField(max_length=40)
    sub_description = models.TextField(max_length=3000, blank=True, null=True)
    duration = models.DurationField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    instructor = models.ForeignKey(User, related_name='instractor_lesson', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="lesson_course", on_delete= models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="lesson_unit")
    video = models.FileField(upload_to='lesson_videos/', blank=True, null=True)
    resources  = models.FileField(upload_to='lesson_resources/', blank=True, null=True)
    assignment = models.BooleanField(default=False)
    slides =  models.FileField(upload_to='lesson_slides/', blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=150, null=True, blank=True)


     

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    

    def __str__(self) -> str:
        return f"{self.title} for course {self.course}"





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
