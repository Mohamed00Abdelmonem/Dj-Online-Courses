from django.contrib import admin
from .models import Course, Review, Lesson, Unit, Quiz, Question, Choice, Notification
from unfold.admin import ModelAdmin



class SimpleAdmin(ModelAdmin):
    list_display = ('title', 'skill_level', 'price', 'avg_rate')

    unfold = {
        'sections': [
            {
                'label': 'Simple Chart',
                'content': {
                    'chart': {
                        'type': 'bar',
                        'data': {
                            'labels': ['A', 'B', 'C'],
                            'datasets': [
                                {
                                    'label': 'Simple Data',
                                    'data': [5, 10, 15],
                                    'backgroundColor': 'rgba(153, 102, 255, 0.2)',
                                    'borderColor': 'rgba(153, 102, 255, 1)',
                                    'borderWidth': 1,
                                },
                            ],
                        },
                    },
                },
            },
        ]
    }

admin.site.register(Course, SimpleAdmin)








class LessonAdmin(ModelAdmin):
    list_display = ('id', 'title', 'course')
    list_filter = ('course',)  # Add filter for course

class UnitAdmin(ModelAdmin):
    list_display = ('id', 'title', 'course')
    list_filter = ('course',)  # Add filter for course

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(ModelAdmin):
    inlines = [ChoiceInline]

# Register the remaining models
admin.site.register(Unit, UnitAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Quiz)
admin.site.register(Review)
admin.site.register(Notification)
admin.site.register(Question, QuestionAdmin)  # Register Question with custom admin class
