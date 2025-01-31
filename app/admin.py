from django.contrib import admin
from .models import Course, Instructor, Lesson, Assignment, Quiz


admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Quiz)