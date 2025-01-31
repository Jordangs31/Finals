from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course, Instructor, Lesson
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Sum

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'app/course_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            filtered_courses = Course.objects.filter(title__icontains=query).order_by('-created_at')
        else:
            filtered_courses = Course.objects.all().order_by('-created_at')
        context['courses'] = filtered_courses
        context['total_courses'] = Course.objects.count()
        context['total_instructors'] = Instructor.objects.count()
        context['total_lessons'] = Lesson.objects.count()
        context['total_users'] = User.objects.count()
        context['sum_course_instructors'] = filtered_courses.aggregate(Sum('instructor'))['instructor__sum'] or 0
        return context

class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'app/course_detail.html'

class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'description', 'instructor', 'user']
    template_name = 'app/course_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['instructors'] = Instructor.objects.all()
        return context






class CourseUpdateView(UpdateView):
    model = Course
    fields = ['title', 'description', 'instructor', 'user']
    template_name = 'app/course_update.html'

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'app/course_delete.html'
    success_url = reverse_lazy('course')

