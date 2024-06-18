from rest_framework import serializers
from .models import Course, Unit, Lesson



class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    lessons = LessonsSerializer(source='lesson_unit', many=True)

    class Meta:
        model = Unit
        fields= '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields= '__all__'



class CourseDetailSerializer(serializers.ModelSerializer):
    units = UnitSerializer(source='unit_course', many=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'image', 'price', 'units']

      
