



import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from courses.models import  Category, Courses, Reviews
from django.utils import timezone
from courses.models import Category, Courses, Reviews
from django.contrib.auth.models import User

fake = Faker()

def create_categories():
    categories = ['Programming', 'Science', 'Mathematics', 'History']
    for category_name in categories:
        Category.objects.create(name=category_name)

def create_courses(num_courses=20):
    categories = Category.objects.all()
    images = ['1.jpg', '2.png', '3.jpeg', '4.jpeg', '5.png', '6.png', '7.png']

    for _ in range(num_courses):
        course = Courses.objects.create(
            name=fake.word(),
            sub_title=fake.text(),
            description=fake.text(),
            image=f'course_cover_image/{fake.random_element(images)}',  # Randomly choose an image filename
            price=fake.random_int(min=10, max=100),
            category=fake.random_element(categories)
        )


def create_users(num_users=5):
    for _ in range(num_users):
        User.objects.create_user(
            username=fake.user_name(),
            password=fake.password()
        )

def create_reviews(num_reviews=20):
    courses = Courses.objects.all()
    users = User.objects.all()
    for _ in range(num_reviews):
        review = Reviews.objects.create(
            user=fake.random_element(users),
            course=fake.random_element(courses),
            review=fake.text(),
            rate=fake.random_int(min=1, max=5),
            created_at=fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
        )

# create_categories()
create_courses()
# create_users()
# create_reviews()
print("Dummy data created successfully.")