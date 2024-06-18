from .serializers import CourseSerializer
from rest_framework import generics
from .models import Course




class CourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()