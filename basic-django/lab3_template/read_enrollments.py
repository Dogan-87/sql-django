# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from related_objects.models import *
from datetime import date


# Your code starts from here:
print("1. Get the user information about learner `David`")
learner_david = Learner.objects.get(first_name="David")
#<HINT> use the usr_ptr field created by Django for the Inheritance relationship# 
print( learner_david.user_ptr)

print("\n")
print("2. Get learner `David` information from user")
user_david = User.objects.get(first_name="David")
#<HINT> use the learner field created by Django# 
print(user_david.learner)

print("\n")
print("3. Get all learners for `Introduction to Python` course")
course = Course.objects.get(name='Introduction to Python')
#<HINT> use the learners field in Course model# 
learners = course.learners.all()
print(learners)

print("\n")
print("4. Check the occupation list for the courses taught by instructor `Yan`")
 #<HINT> query the first name of instructor# 
courses = Course.objects.filter(instructors__first_name='Yan')
occupation_list = set()
for course in courses:
    #<HINT>use the learners field in Course Model#
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print(occupation_list)

print("\n")
print("5. Check which courses developers are enrolled in Aug, 2020")  
enrollments = Enrollment.objects.filter(date_enrolled__month=8,
                                            date_enrolled__year=2020,
                                            #<HINT>use the occupation field from learner #
                                            learner__occupation='developer')
courses_for_developers = set()
for enrollment in enrollments:
    course = enrollment.course
    courses_for_developers.add(course.name)
print(courses_for_developers)