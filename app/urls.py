from django.urls import path
from .views import (HomePageView, AboutPageView, CourseListView, 
                    CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', CourseListView.as_view(), name='course'),
    path('blog/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('blog/create', CourseCreateView.as_view(), name='course_create'),
    path('blog/<int:pk>/edit', CourseUpdateView.as_view(), name='course_update'),
    path('blog/<int:pk>/delete', CourseDeleteView.as_view(), name='course_delete'),

]