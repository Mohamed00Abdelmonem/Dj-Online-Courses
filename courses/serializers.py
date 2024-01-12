from rest_framework import serializers
from .models import Category, Courses, Reviews
from django.db.models.aggregates import Avg



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'




class CoursesSerializer(serializers.ModelSerializer):
    avg_rate= serializers.SerializerMethodField()
    class Meta:
        model = Courses

        fields = '__all__'

    def get_avg_rate(self, review):
        avg = review.courses_review.aggregate(rate_avg=Avg('rate'))
        if avg['rate_avg'] is not None:
            return avg['rate_avg']
        else:
            return 0
   



class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
