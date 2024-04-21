from django.contrib import admin
from .models import Course, Review, Lesson, Unit, Quiz, Question, Choice, Notification

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course')
    list_filter = ('course',)  # Add filter for course

class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course')
    list_filter = ('course',)  # Add filter for course

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Course)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Quiz)
admin.site.register(Review)
admin.site.register(Notification)
admin.site.register(Question, QuestionAdmin)  # Register Question with custom admin class
