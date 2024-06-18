from .serializers import CourseSerializer, CourseDetailSerializer
from rest_framework import generics
from .models import Course, Unit




class CourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()



class CourseDetail(generics.RetrieveDestroyAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()