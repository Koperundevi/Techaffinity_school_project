from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from axes.decorators import watch_login
from django.middleware.csrf import CsrfViewMiddleware
from django.views.decorators.csrf import csrf_exempt
import os
from django.contrib.auth.models import Permission, Group, User, ContentType, AnonymousUser
from django.contrib.auth import login, logout , authenticate, get_user_model
import datetime
from django.core.urlresolvers import reverse,resolve
from models import *
from django.db.models import Sum
from django_pandas.io import read_frame
import numpy as np
from django.db.models import Q
from permissions import authentication_permission_check

@authentication_permission_check()
def home(request):
    user = request.user
    teacher_obj = Teacher.objects.filter(user_id = user.id).first()
    return render(request, 'home.html', {'teacher':teacher_obj})

@authentication_permission_check()
def assign_marks(request):
    user = request.user
    teacher_obj = Teacher.objects.filter(user_id = user.id).first()
    student_list = Mark.objects.filter(subject_id = teacher_obj.subject_id).values_list('student_id',flat=True)
    student_obj = Student.objects.all().exclude(id__in = student_list)
    return render(request, 'assign_marks.html', {'teacher':teacher_obj,'student_obj':student_obj})

@authentication_permission_check()
def edit_marks(request):
    user = request.user
    teacher_obj = Teacher.objects.filter(user_id = user.id).first()
    marks_obj = Mark.objects.filter(subject_id = teacher_obj.subject_id)
    return render(request, 'edit_marks.html', {'teacher':teacher_obj, 'marks_obj':marks_obj})

@authentication_permission_check(superuser_required=True)
def generate_rank(request):
    user = request.user
    total_obj = Mark.objects.all().values('student__id','student__name','student__rank').annotate(score = Sum('score')).order_by('-score')
    mark_added_subjects = Mark.objects.all().values_list('subject__id', flat=True).distinct()
    empty_subject_obj = Subject.objects.all().exclude(id__in = mark_added_subjects).values_list('name', flat=True)
    empty_rank_obj = Student.objects.filter(Q(rank = 0)| Q(rank__isnull = True))
    df = read_frame(total_obj)
    if empty_rank_obj:
        df['student__rank'] = df['score'].rank(ascending=0)
        df["student__rank"] = df['student__rank'].astype(np.int64)

    return_dict = {'total_obj':total_obj, 'dataframe':df, 'empty_rank_obj':empty_rank_obj, 'empty_subject_obj':empty_subject_obj}
    if request.POST and empty_rank_obj:
        for i in df.itertuples():
            student_obj = Student.objects.get(id = i.student__id)
            student_obj.rank = i.student__rank
            student_obj.save()
        return_dict.update({'message': 'Successfully generated and submitted the rank for students', 'empty_rank_obj':None})

    return render(request, 'generate_rank.html', return_dict)

@authentication_permission_check(superuser_required=True)
def add_students_in_bulk(request):
    return render(request, 'add_students_in_bulk.html')

# Login View 
@watch_login   
def teacher_login(request):
    user_obj, msg = request.user, None
    if user_obj.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
   
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    if 'HTTP_REFERER' in request.META:
        if request.META['HTTP_REFERER'].split('/')[-2] == 'forgot_password':
            return_dict['msg'] = 'An email is sent. Please check your email.'
    if request.POST:
        data = request.POST
        user = authenticate(username = data.get('username'), password = data.get('password'))
        if not user or not user.is_active:
            return_dict['msg'] = "The username and password is incorrect."
            return render(request, 'customer/login.html', return_dict)

        login(request, user)
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'login.html', {})

# Logout View 
def teacher_logout(request):
    user_login = 'teacher_login'
    if request.user.is_authenticated():
        if hasattr(request, 'user'):
            request.user = AnonymousUser()
        logout(request)

    return HttpResponseRedirect(reverse(user_login))
