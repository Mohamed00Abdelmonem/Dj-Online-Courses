from .serializers import CourseSerializer, CourseDetailSerializer
from rest_framework import generics
from .models import Course, Unit
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters






@method_decorator(cache_page(60 * 60 * 2), name='dispatch')
class CourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields  = ['tilte']
    ordering_fields = ['price']


class CourseDetail(generics.RetrieveDestroyAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()