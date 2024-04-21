import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from courses.models import Course, Lesson, Unit, Review, Question, Quiz, Choice
from django.contrib.auth.models import User
from datetime import timedelta
from taggit.models import Tag
from django.utils.text import slugify



def seed_courses(n):
    fake = Faker('en_US')
    skill_level = ['Beginner', 'Intermediate', 'Advanced']
    language = ['Arabic', 'English', 'French']
    tags = ['Python', 'Django', 'JavaScript', 'React', 'HTML', 'CSS']  # Define your tags
    users = User.objects.all()

    images = ['1 (1).png', '1 (10).png', '1 (11).png', '1 (12).png', '1 (2).png', '1 (3).png', '1 (4).png', '1 (5).png', '1 (6).png', '1 (7).png', '1 (8).png', '1 (9).png', '1 (1).jpg', '1 (2).jpg', '1 (3).jpg', '1 (1).jpeg', '1 (10).jpeg', '1 (11).jpeg', '1 (12).jpeg', '1 (13).jpeg', '1 (14).jpeg', '1 (15).jpeg', '1 (2).jpeg', '1 (3).jpeg', '1 (4).jpeg', '1 (5).jpeg', '1 (6).jpeg', '1 (7).jpeg', '1 (8).jpeg', '1 (9).jpeg']
    
    for _ in range(n):
        # Generate a random duration using timedelta
        duration_days = random.randint(1, 10)
        duration = timedelta(days=duration_days)

        # Choose a random user's ID
        random_user_id = fake.random_element(users).id

        # Generate a unique slug for the course title
        title = fake.name()
        slug = slugify(title)
        while Course.objects.filter(slug=slug).exists():
            slug = f"{slug}-{fake.random_number(digits=4)}"

        # Choose random tags for the course
        num_tags = random.randint(1, 3)  # Choose between 1 to 3 tags per course
        chosen_tags = random.sample(tags, num_tags)

        course = Course.objects.create(
            title=title,
            user_id=random_user_id,
            image=f'course_images/{images[random.randint(0, 29)]}',
            price=round(random.uniform(20.99, 99.99), 2),
            skill_level=skill_level[random.randint(0, 2)], 
            duration=duration,
            rate=random.randint(0, 4),
            language=language[random.randint(0, 2)],
            description=fake.text(max_nb_chars=1000),
            slug=slug
        )

        course.tags.add(*chosen_tags)

    print(f"Seeded {n} Courses Successfully")



def seed_quizzes_and_questions(n):
    fake = Faker()
    units = Unit.objects.all()

    for _ in range(n):
        title = fake.sentence(nb_words=4)
        duration = random.randint(10, 60)  # Assuming duration in minutes
        unit = random.choice(units)
        quiz = Quiz.objects.create(
            unit=unit,
            title=title,
            duration=duration,
        )

        print(f"Seeded quiz: {quiz.title}")

        # Create questions for the quiz
        for _ in range(random.randint(3, 5)):  # You can adjust the number of questions as needed
            question_text = fake.sentence(nb_words=10)  # Generate a random sentence for question text
            question = Question.objects.create(quiz=quiz, text=question_text)

            print(f"Seeded question: {question.text}")

            # Create choices for each question
            for _ in range(random.randint(2, 4)):  # You can adjust the number of choices as needed
                choice_text = fake.sentence(nb_words=6)
                is_correct = fake.boolean(chance_of_getting_true=30)  # Adjust probability of correct choice
                choice = Choice.objects.create(question=question, text=choice_text, is_correct=is_correct)

                print(f"Seeded choice: {choice.text}")

    print(f"Seeded {n} Quizzes, Questions, and Choices Successfully")




def seed_units(n):
    fake = Faker()
    courses = Course.objects.all()

    for _ in range(n):
        title = fake.sentence(nb_words=4)
        course = random.choice(courses)
        slug = slugify(title)

        # Ensure slug uniqueness
        while Unit.objects.filter(slug=slug).exists():
            slug = f"{slug}-{fake.random_number(digits=4)}"

        unit = Unit.objects.create(
            title=title,
            course=course,  # This should be 'course_id' instead of 'Course'
            slug=slug
        )

        print(f"Seeded unit: {unit.title}")

    print(f"Seeded {n} Units Successfully")




def seed_lessons(n):
    fake = Faker()
    users = User.objects.all()
    courses = Course.objects.all()
    units = Unit.objects.all()
    lesson_resources = ['1 (1).pdf', '1 (2).pdf', '1 (3).pdf', '1 (4).pdf']
    lesson_slides = ['1 (1).pdf', '1 (2).pdf', '1 (3).pdf', '1 (4).pdf', '1 (5).pdf', '1 (6).pdf']
    videos = ['1 (1).mp4', '1 (2).mp4', '1 (3).mp4', '1 (4).mp4', '1 (5).mp4', '1 (6).mp4', '1 (7).mp4']

    for _ in range(n):
        title = fake.sentence(nb_words=4)
        sub_description = fake.paragraph(nb_sentences=3)
        duration = timedelta(minutes=random.randint(15, 90))
        created_at = fake.date_time_this_year()
        instructor = random.choice(users)
        course = random.choice(courses)
        unit = random.choice(units)
        video = f'course_videos/{random.choice(videos)}'
        resources = f'lesson_resources/{random.choice(lesson_resources)}'
        assignment = fake.boolean(chance_of_getting_true=50)
        slides = f'lesson_slides/{random.choice(lesson_slides)}'
        slug = slugify(title)

        # Ensure slug uniqueness
        while Lesson.objects.filter(slug=slug).exists():
            slug = f"{slug}-{fake.random_number(digits=4)}"

        lesson = Lesson.objects.create(
            title=title,
            sub_description=sub_description,
            duration=duration,
            created_at=created_at,
            instructor=instructor,
            course=course,
            unit=unit,
            video=video,
            resources=resources,
            assignment=assignment,
            slides=slides,
            slug=slug
        )

        print(f"Seeded lesson: {lesson.title}")

    print(f"Seeded {n} Lessons Successfully")





def seed_reviews(n):
    fake = Faker()
    users = User.objects.all()
    courses = Course.objects.all()

    for _ in range(n):
        course = random.choice(courses)
        Review.objects.create(
            user=fake.random_element(users),
            course=course,
            rate=random.randint(0, 4),
            comment=fake.text(max_nb_chars=250),
        )

    print(f"Seeded {n} Reviews Successfully")

seed_courses(100)
seed_units(300)
seed_lessons(700)
seed_reviews(700)
# create_users(5)
seed_quizzes_and_questions(300)