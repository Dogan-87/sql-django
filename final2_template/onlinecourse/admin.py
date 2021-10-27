from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    #inlines = [QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    #added to see questions in Lesson section
    #inlines = [QuestionInline]
#
class QuestionAdmin(admin.ModelAdmin):
    list_display = [ 'course_id', 'question_text', 'grade']
    #inlines = [ChoiceInline]
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'is_correct']

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
#
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)