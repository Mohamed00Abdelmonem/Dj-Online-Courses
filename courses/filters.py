from django_filters import rest_framework as filters
from taggit.models import Tag
from taggit.managers import TaggableManager
from .models import Course

class CourseFilter(filters.FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        to_field_name='name',  # Filter courses by tag names
    )

    class Meta:
        model = Course
        fields = ['title', 'price', 'tags']
        filter_overrides = {
            TaggableManager: {
                'filter_class': filters.ModelMultipleChoiceFilter,
                'extra': lambda f: {
                    'queryset': Tag.objects.all(),
                },
            },
        }
