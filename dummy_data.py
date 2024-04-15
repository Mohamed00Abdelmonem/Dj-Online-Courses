import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from courses.models import Course, Lesson, Unit, Review
from django.contrib.auth.models import User
from datetime import timedelta
from taggit.models import Tag





from django.utils.text import slugify

def seed_courses(n):
    fake = Faker('en_US')
    skill_level = ['Beginner', 'Intermediate', 'Advanced']
    language = ['Arabic', 'English', 'French']
    tags = ['python', 'html', 'programming', 'code', 'basics']
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

        Course.objects.create(
            title=title,
            user_id=random_user_id,
            image=f'course_images/{images[random.randint(0, 29)]}',
            price=round(random.uniform(20.99, 99.99), 2),
            skill_level=skill_level[random.randint(0, 2)], 
            duration=duration,
            rate=random.randint(0, 4),
            language=language[random.randint(0, 2)],
            description=fake.text(max_nb_chars=1000),
            tags=tags[random.randint(0, 4)],
            slug=slug
        )

    print(f"Seeded {n} Courses Successfully")



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

    for _ in range(n):
        title = fake.sentence(nb_words=4)
        sub_description = fake.paragraph(nb_sentences=3)
        duration = timedelta(minutes=random.randint(15, 90))
        created_at = fake.date_time_this_year()
        instructor = random.choice(users)
        course = random.choice(courses)
        unit = random.choice(units)
        video = fake.file_path(depth=2, category='video')
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






# def seed_courses(n):
#     fake = Faker('en_US')
#     skill_level = ['Beginner', 'Intermediate', 'Advanced']
#     language = ['Arabic', 'English', 'French']
#     tags = ['python', 'html', 'programming', 'code', 'c', 'hello_world', 'beginner', 'basics']
#     users = User.objects.all()

#     images = ['1 (1).png', '1 (10).png', '1 (11).png', '1 (12).png', '1 (2).png', '1 (3).png', '1 (4).png', '1 (5).png', '1 (6).png', '1 (7).png', '1 (8).png', '1 (9).png', '1 (1).jpg', '1 (2).jpg', '1 (3).jpg', '1 (1).jpeg', '1 (10).jpeg', '1 (11).jpeg', '1 (12).jpeg', '1 (13).jpeg', '1 (14).jpeg', '1 (15).jpeg', '1 (2).jpeg', '1 (3).jpeg', '1 (4).jpeg', '1 (5).jpeg', '1 (6).jpeg', '1 (7).jpeg', '1 (8).jpeg', '1 (9).jpeg']
    
#     for _ in range(n):
#         # Generate a random duration using timedelta
#         duration_days = random.randint(1, 10)
#         duration = timedelta(days=duration_days)

#         # Choose a random user's ID
#         random_user_id = fake.random_element(users).id

#         # Choose random tags for the course
#         num_tags = random.randint(1, 3)  # Choose between 1 to 3 tags per course
#         chosen_tags = random.sample(tags, num_tags)

#         course = Course.objects.create(
#             title=fake.name(),
#             user_id=random_user_id,
#             image=f'course_images/{images[random.randint(0, 29)]}',
#             price=round(random.uniform(20.99, 99.99), 2),
#             skill_level=random.choice(skill_level), 
#             duration=duration,
#             rate=random.randint(0, 4),
#             language=random.choice(language),
#             description=fake.text(max_nb_chars=1000),
#         )

#         # Assign the chosen tags to the course
#         course.tags.add(*chosen_tags)

#     print(f"Seeded {n} Courses Successfully")


# def seed_unit(n):
#     fake = Faker()
#     for _ in range(n):
#         Unit.objects.create(
#             title=fake.name(),
#             Course =  Course.objects.get(id=random.randint(1,150)),

#                             )
#     print(f"Seeded {n} Unit Successfully")




# def seed_product(n):
#     fake = Faker()
#     images = ['14.png', '36.png', '40.png', '5.png', '7.png', '70.png', '10.jpg', '19.jpg', 
# '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '29.jpg', '37.jpg', '38.jpg', '39.jpg', '41.jpg', '42.jpg', '43.jpg', '44.jpg', '45.jpg', '46.jpg', '47.jpg', '48.jpg', '49.jpg', '5.jpg', '51.jpg', '52.jpg', '53.jpg', '54.jpg', '55.jpg', '56.jpg', '57.jpg', '58.jpg', '59.jpg', '6.jpg', '60.jpg', '61.jpg', '62.jpg', '63.jpg', '64.jpg', '65.jpg', '66.jpg', '67.jpg', '68.jpg', '69.jpg', '8.jpg', '9.jpg', '100.jpeg', '101.jpeg', '102.jpeg', '103.jpeg', '104.jpeg', '105.jpeg', '106.jpeg', '107.jpeg', '108.jpeg', '109.jpeg', '11.jpeg', '110.jpeg', '111.jpeg', '112.jpeg', '113.jpeg', '114.jpeg', '115.jpeg', '116.jpeg', '117.jpeg', '118.jpeg', '119.jpeg', '12.jpeg', '120.jpeg', '121.jpeg', '122.jpeg', '123.jpeg', '124.jpeg', '125.jpeg', '126.jpeg', '127.jpeg', '128.jpeg', '129.jpeg', '13.jpeg', '130.jpeg', '131.jpeg', '15.jpeg', '16.jpeg', '17.jpeg', '18.jpeg', '2.jpeg', '25.jpeg', '26.jpeg', '27.jpeg', '28.jpeg', '3.jpeg', '30.jpeg', '31.jpeg', '32.jpeg', '33.jpeg', '34.jpeg', '35.jpeg', '50.jpeg', '71.jpeg', '72.jpeg', '73.jpeg', '74.jpeg', '75.jpeg', '76.jpeg', '77.jpeg', '78.jpeg', '79.jpeg', '8.jpeg', '80.jpeg', '81.jpeg', '82.jpeg', '83.jpeg', '84.jpeg', '85.jpeg', '86.jpeg', '87.jpeg', '88.jpeg', '89.jpeg', '90.jpeg', '91.jpeg', '92.jpeg', '93.jpeg', '94.jpeg', '95.jpeg', '96.jpeg', '97.jpeg', '98.jpeg', '99.jpeg', '18.webp', '19.webp', '32.webp', '5.webp']
#     flags = ['new', 'sale', 'feature']
#     for _ in range(n):
#         Product.objects.create(
#             name = fake.name(),
#             image = f'products/{images[random.randint(0,134)]}',
#             flag = flags[random.randint(0, 2)],
#             price = round(random.uniform(20.99, 99.99),2),
#             sku = random.randint(1000,100000) ,
#             rate = random.randint(0,4) ,
#             subtitle = fake.text(max_nb_chars=250),
#             description = fake.text(max_nb_chars=2000),
#             quantity = random.randint(0,30),
#             brand = Brand.objects.get(id=random.randint(1,20)),

#         )

#     print(f"Seed {n} Products Successfully")


# def seed_product_images(n):
#     fake = Faker()
#     images = ['14.png', '36.png', '40.png', '5.png', '7.png', '70.png', '10.jpg', '19.jpg', 
# '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '29.jpg', '37.jpg', '38.jpg', '39.jpg', '41.jpg', '42.jpg', '43.jpg', '44.jpg', '45.jpg', '46.jpg', '47.jpg', '48.jpg', '49.jpg', '5.jpg', '51.jpg', '52.jpg', '53.jpg', '54.jpg', '55.jpg', '56.jpg', '57.jpg', '58.jpg', '59.jpg', '6.jpg', '60.jpg', '61.jpg', '62.jpg', '63.jpg', '64.jpg', '65.jpg', '66.jpg', '67.jpg', '68.jpg', '69.jpg', '8.jpg', '9.jpg', '100.jpeg', '101.jpeg', '102.jpeg', '103.jpeg', '104.jpeg', '105.jpeg', '106.jpeg', '107.jpeg', '108.jpeg', '109.jpeg', '11.jpeg', '110.jpeg', '111.jpeg', '112.jpeg', '113.jpeg', '114.jpeg', '115.jpeg', '116.jpeg', '117.jpeg', '118.jpeg', '119.jpeg', '12.jpeg', '120.jpeg', '121.jpeg', '122.jpeg', '123.jpeg', '124.jpeg', '125.jpeg', '126.jpeg', '127.jpeg', '128.jpeg', '129.jpeg', '13.jpeg', '130.jpeg', '131.jpeg', '15.jpeg', '16.jpeg', '17.jpeg', '18.jpeg', '2.jpeg', '25.jpeg', '26.jpeg', '27.jpeg', '28.jpeg', '3.jpeg', '30.jpeg', '31.jpeg', '32.jpeg', '33.jpeg', '34.jpeg', '35.jpeg', '50.jpeg', '71.jpeg', '72.jpeg', '73.jpeg', '74.jpeg', '75.jpeg', '76.jpeg', '77.jpeg', '78.jpeg', '79.jpeg', '8.jpeg', '80.jpeg', '81.jpeg', '82.jpeg', '83.jpeg', '84.jpeg', '85.jpeg', '86.jpeg', '87.jpeg', '88.jpeg', '89.jpeg', '90.jpeg', '91.jpeg', '92.jpeg', '93.jpeg', '94.jpeg', '95.jpeg', '96.jpeg', '97.jpeg', '98.jpeg', '99.jpeg', '18.webp', '19.webp', '32.webp', '5.webp']
#     for _ in range(n):
#         ProductImages.objects.create(
#             product = Product.objects.get(id=random.randint(0,90)),
#             image = f'product_images/{images[random.randint(0,134)]}'
#         )

#     print(f"Seed {n} images in product Successfully")







# def create_users(n):
#     fake = Faker()
#     for _ in range(n):
#         User.objects.create_user(
#             username=fake.user_name(),
#             password=fake.password()
#     )
#     print(f"Seed {n} Reviews Successfully")
    




import random

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

# seed_courses(100)
seed_units(100)
# seed_lessons(10)
# seed_reviews(60)
# create_users(5)