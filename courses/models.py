from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg
from taggit.managers import TaggableManager
from django.utils import timezone


# _________________________________________________________________________________________

class Course(models.Model):
    image = models.ImageField(upload_to='course_images/')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Teachers'})
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

    def avg_rate(self):
        avg = self.reviews.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']
    
    def __str__(self) -> str:
        return self.title

# _________________________________________________________________________________________

class Lesson(models.Model):
    title = models.CharField(max_length=40)
    sub_description = models.TextField(max_length=3000, blank=True, null=True)
    duration = models.DurationField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    instructor = models.ForeignKey(User, related_name='instractor_lesson', on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Teachers'})
    course = models.ForeignKey(Course, related_name="lesson_course", on_delete= models.CASCADE)
    veido = models.FileField(upload_to='lesson_videos/', blank=True, null=True)
    resources  = models.FileField(upload_to='lesson_resources/', blank=True, null=True)
    assignment = models.BooleanField(default=False)
    slides =  models.FileField(upload_to='lesson_slides/', blank=True, null=True)



    def __str__(self) -> str:
        return f"{self.title} for course {self.course}"





# _________________________________________________________________________________________


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.FloatField()
    comment = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.comment[:20]} for course {self.course}"

# _________________________________________________________________________________________
