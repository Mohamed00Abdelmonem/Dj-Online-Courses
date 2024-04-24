from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Course, Review, Lesson, Unit, Quiz, Question, Choice, Notification
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




# ____________________________________________________________________________

class Course_Grid(ListView):
    model = Course
    template_name = 'course-grid.html'
    context_object_name = 'courses'
    paginate_by = 15  
    ordering = ['-id']
   

# ____________________________________________________________________________



class Course_List(ListView):
    model = Course
    template_name = 'course-list.html'
    context_object_name = 'courses'
    ordering = ['-id']
    paginate_by = 15

# ____________________________________________________________________________

class Course_Detail(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course-details.html'
    
    # slug_url_kwarg = 'slug'  # specify the slug URL keyword


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_course = self.get_object()
        # current_lessons = Lesson.objects.filter(course =current_course)
        related_unit = Unit.objects.filter(course=current_course )
          # Create a dictionary to store units and their corresponding lessons
        unit_lessons = {}

        # Iterate over each unit and retrieve its associated lessons
        for unit in related_unit:
            unit_lessons[unit] = unit.lesson_unit.all()

        related_courses = Course.objects.filter(tags__in=current_course.tags.all()).exclude(id=current_course.id).distinct()
        context["related_courses"] = related_courses
        context["related_unit"] = related_unit
        context["unit_lessons"] = unit_lessons
        # context["current_lessons"] = current_lessons
        context["current_course"] = current_course


        return context
    
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
