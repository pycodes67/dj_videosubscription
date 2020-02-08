from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Course, Lesson
from memberships.models import UserMembership
from django.contrib.auth.decorators import login_required



class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'


class LessonDetailView(View):

    def get(self, request, course_slug, lesson_slug, *args, **kwargs):

        course = get_object_or_404(Course, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        user_membership = get_object_or_404(UserMembership, user=request.user)
        user_membership_type = user_membership.membership.membership_type
        course_allowed_mem_types = course.allowed_memberships.all()
        
        context = { 'object': None }

        if course_allowed_mem_types.filter(membership_type=user_membership_type).exists() or course_allowed_mem_types.filter(membership_type='Free'):
            context = {'object': lesson}
        return render(request, "lesson_detail.html", context)
