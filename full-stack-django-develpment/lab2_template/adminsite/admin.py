from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.

class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']

#associate related objects on a single model managing page. This can be done by defining Inline classes
class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    #update CourseAdmin class by adding a inlines list
    inlines = [LessonInline]

#admin.site.register(Instructor) hanged to include some of the model fields in the admin site.
admin.site.register(Instructor, InstructorAdmin)

#admin.site.register(Course) changed to include some of the model fields in the admin site.
admin.site.register(Course, CourseAdmin)

