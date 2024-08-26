from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Course, Review, Lesson, Unit, Quiz, Question, Choice, Notification
from taggit.models import Tag
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Profile
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Course
import logging
from django.db.models import Count

# ____________________________________________________________________________


# create logger
logger = logging.getLogger('db') # name = app.views (courses.views)
class Course_Grid(ListView):
    
    model = Course
    template_name = 'course-grid.html'
    context_object_name = 'courses'
    paginate_by = 15  
    ordering = ['-id']

    def get(self, request, *args, **kwargs):
        try:
            # logger
            logger.info('Course_grid view accessed')
            return super().get(request, *args, **kwargs)
        except Exception as e:
            # logger
            logger.error(f'Course_grid view error: {e}')
            raise
   

# ____________________________________________________________________________



from django.shortcuts import render
from .models import Course

def filter_courses(request):
    if request.is_ajax():
        level = request.GET.getlist('level')
        max_price = request.GET.get('price')

        courses = Course.objects.all()

        if level:
            courses = courses.filter(level__in=level)
        if max_price:
            courses = courses.filter(price__lte=max_price)

        return render(request, 'partials/course_list.html', {'courses': courses})
    else:
        # Normal rendering for the page
        courses = Course.objects.all()
        return render(request, 'course_list.html', {'courses': courses})




# ____________________________________________________________________________



from django.db.models import Count, Q
from django.views.generic import ListView
from .models import Course
from taggit.models import Tag

class CourseListView(ListView):
    model = Course
    template_name = 'course-list.html'
    context_object_name = 'courses'
    paginate_by = 15  # Show 15 courses per page

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Initialize a Q object for dynamic filtering
        filters = Q()

        # Filtering by skill level
        skill_level = self.request.GET.get('skill_level')
        if skill_level:
            filters &= Q(skill_level=skill_level)

        # Filtering by price range
        price_min = self.request.GET.get('price_min', 0)
        price_max = self.request.GET.get('price_max', 1000)
        filters &= Q(price__gte=price_min, price__lte=price_max)

        # Filtering by tags
        selected_tags = self.request.GET.getlist('tags')
        if selected_tags:
            filters &= Q(tags__name__in=selected_tags)

        # Apply the filters to the queryset
        queryset = queryset.filter(filters).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the filtered queryset to count the number of courses after filtering
        filtered_queryset = self.get_queryset()
        context['filtered_course_count'] = filtered_queryset.count()

        # Include other context data as needed
        context['price_min'] = self.request.GET.get('price_min', 0)
        context['price_max'] = self.request.GET.get('price_max', 1000)
        context['skill_level_filter'] = self.request.GET.get('skill_level')
        context['selected_tags'] = self.request.GET.getlist('tags')
        context['tags'] = Tag.objects.annotate(num_courses=Count('course')).order_by('-num_courses')
        
        return context


# ____________________________________________________________________________

class Course_Detail(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course-details.html'
    
    # slug_url_kwarg = 'slug'  # specify the slug URL keyword

    def get_context_data(self, **kwargs):
        """
        This method adds extra context to the template.
        """
        context = super().get_context_data(**kwargs)
        current_course = self.get_object()
        
        # Log the current course being processed
        logger.debug(f'Fetching context data for course: {current_course}')
        
        try:
            # Fetch related units
            related_unit = Unit.objects.filter(course=current_course)
            logger.debug(f'Related units: {related_unit}')
            
            # Create a dictionary to store units and their corresponding lessons
            unit_lessons = {}

            # Iterate over each unit and retrieve its associated lessons
            for unit in related_unit:
                unit_lessons[unit] = unit.lesson_unit.all()  # Retrieve lessons for each unit
                logger.debug(f'Unit: {unit}, Lessons: {unit_lessons[unit]}')

            # Fetch related courses excluding the current course
            related_courses = Course.objects.filter(tags__in=current_course.tags.all()).exclude(id=current_course.id).distinct()
            logger.debug(f'Related courses: {related_courses}')

            # Add related courses, units, and lessons to the context
            context["related_courses"] = related_courses
            context["related_unit"] = related_unit
            context["unit_lessons"] = unit_lessons
            context["current_course"] = current_course

        except Exception as e:
            # Log any errors that occur during the context data fetching
            logger.error(f'Error fetching context data: {e}')
            raise
        
        return context
    
    def dispatch(self, request, *args, **kwargs):
        """
        This method is called when the view is accessed. It ensures that 
        the user is authenticated and handles HTTP exceptions.
        """
        try:
            # Log access to the Course_Detail view
            logger.info('Course_Detail view accessed')
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            # Log a warning if the course is not found and return a 404 page
            logger.warning('Course_Detail view accessed, but course not found')
            return render(request, 'page404.html', status=404)
        except Exception as e:
            # Log any unexpected errors and return a 500 error page
            logger.error(f'Unexpected error in dispatch: {e}')
            return render(request, 'page500.html', status=500)
        
# ____________________________________________________________________________
@login_required

def add_review(request, slug):
        course = Course.objects.get(slug=slug)
        rate = request.POST['rate']
        review = request.POST['review']
        
        Review.objects.create(
            course=course,
            rate=rate,
            comment=review,
            user=request.user
        )

        return redirect(f'/courses/{course.slug}')


# ____________________________________________________________________________



class LessonList(ListView):
    model = Lesson
    template_name = 'lesson-list.html'
    context_object_name = 'lessons'


    def get_queryset(self):
        course = Course.objects.get(id=self.kwargs['course_pk']) # this inectance course
        queryset_lessons = Lesson.objects.filter(course=course)
        return queryset_lessons



# ____________________________________________________________________________




class Lesson_Detail(DetailView):
    model = Lesson
    template_name = 'lesson-details.html' 

# ____________________________________________________________________________



@login_required

def pdf_view_resources(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)

    # Check if any file is associated with the lesson
    if lesson.resources:
        # Proceed with serving the file
        response = HttpResponse(lesson.resources.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{lesson.resources.name}"'
        return response
    else:
        # Handle case where file is missing
        return HttpResponse("This lesson does not have a PDF file associated with it.")


# ____________________________________________________________________________


@login_required

def pdf_view_slides(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)

    # Check if any file is associated with the lesson
    if lesson.slides:
        # Proceed with serving the file
        response = HttpResponse(lesson.slides.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{lesson.slides.name}"'
        return response
    else:
        # Handle case where file is missing
        return HttpResponse("This lesson slides does not have a PDF file associated with it.")
    

# ____________________________________________________________________________

@login_required

def quiz(request, slug, course_slug):
    quiz = get_object_or_404(Quiz, slug=slug)
    
    if request.method == 'POST':
        score = 0
        # Loop through submitted answers
        for question in quiz.questions.all():
            submitted_choice_id = request.POST.get('question{}'.format(question.id))
            # Check if the submitted choice is correct
            if submitted_choice_id:
                submitted_choice = Choice.objects.get(id=submitted_choice_id)
                if submitted_choice.is_correct:  # Use is_correct instead of correct
                    score += 1
        
        # Calculate score percentage
        total_questions = quiz.questions.count()
        score_percentage = (score / total_questions) * 100
        
        return render(request, 'quiz_result.html', {'score_percentage': score_percentage})
    
    return render(request, 'quiz.html', {'quiz': quiz})

# ____________________________________________________________________________



def notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user)
    else:
        notifications = []
    return render(request, 'notification.html', {'notifications': notifications})

# _________________________________________________________________________________________


class InstractorDetial(DetailView):
    model = User
    template_name = 'instructor-profile.html'
    

# _________________________________________________________________________________________



# def instractor_profile(request):
#     return render(request, 'instructor-profile.html')
