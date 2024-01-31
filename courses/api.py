from .models import Category, Courses, Reviews
from .serializers import CategorySerializer, CoursesSerializer,ReviewsSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


class CategoryAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CoursesAPI(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer   
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'price'] 
    ordering_fields = ['name', 'id']
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


class CoursesDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer    




class ReviewsAPI(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer        