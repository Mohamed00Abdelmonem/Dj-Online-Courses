Tasks : 
 today 1-7-2024
     make full api for courses and filtering and make api for auth and carts and 
     make pagination for related courses 



Features in this project online courses

- list , detail cousers   ====> True
- list , detail lessons   ====> True
- reviews in courses      ====> True
- quize for lessons       ====> Inprogress
- make notifactions and send email ===> Inprogress 
- soical login ===> 
- upload document pdf  ===> True
- make auth ===> True
- using celery, caching , docker 
- dummy_data , add debug toblar  = True
- apply coupon 
- strip payment
- close lessons before payment 
- make permessions for student and instractors
- make notifactions for add new lesson  = Insprogress
- send emails for all students 
- add new theme in admin_banal using django = make this at  today 
- make Apis for this project ......






apps in my project online courses
 1- settings
 2- accounts
 3- courses
 4- orders or subscriptions



models app settings

- Company
 - name
 - logo
 - carousel image 1 
 - carousel image 2
 - descriptions
 - about-us (add sumernote)
 - phone1
 - phone2
 - address 1,2
 - email
 - socail-media-facebook
 - socail-media-watsapp
 - socail-media-youtube
 - socail-media-another_link

_______________________________________________________________


models app courses

- Courses 
 - image
 - Instructor (user)
 - title
 - rate
 - price 
 - introduction-video
 - Duration
 - Skill Level
 - Language
 - Certificate (yes or no)
 - descriptions
 - tags 
 

- Lessons
 - title
 - sub desctiption
 - duration
 - teacher (fk)
 - courses (fk)
 - veido 
 - 
 


- Review 
 - user
 - created_at
 - rate
 - comment


_______________________________________________________________


models accounts

- Instractors_profile
 - name 
 - user (one2one limit_choices_to={'groups__name': 'Teachers'})
 - image
 - sub-descriptions
 - Job Title
 - Phone
 - Email
 - Experiences
 - Skill Level
 - Language use
 - courses (forignkey in app courses)
 - about-for-instractor
 - socail-media-facebook
 - socail-media-twitter
 - socail-media-youtube
 - socail-media-instgram




