# InBuilt Import
import json, datetime, base64, pycountry, re, copy, difflib, \
urllib, hashlib, random, os, pytz, calendar, ast, time, string
from decimal import Decimal
from datetime import timedelta
from copy import deepcopy
# Django import
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login
from django.db import transaction, connection
from django.db.models import Q, Min, Sum, Count
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.conf.urls import url
from django.utils import timezone
from django.utils.http import urlencode
from django.forms.models import model_to_dict
from django.db.models.query import QuerySet
from django.db.models import Prefetch
# Send mail
from django.conf import settings
from django.core.cache import cache
# Tastypie import
from tastypie import fields
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.http import HttpAccepted
from tastypie.exceptions import Unauthorized
from tastypie.resources import ModelResource
from web.models import *


class MarkResource(ModelResource):
    
    class Meta:
        queryset = Mark.objects.all()
        authorization = Authorization()
        allowed_methods = ['post', 'get', 'patch']
        resource_name = 'mark'
        always_return_data = True


    def obj_create(self, bundle, **kwargs):
        request_user, input_data = bundle.request.user, bundle.data
        teacher_id, subject_id, data = input_data.get('teacher_id'), input_data.get('subject_id'), input_data.get('data')
        try:
            teacher_obj = Teacher.objects.get(id = teacher_id)
        except:
            raise Exception("Invalid teacher")
        try:
            subject_obj = Subject.objects.get(id = subject_id)
        except:
            raise Exception("Invalid suject")

        marks_list = []
        for i in data:
            try:
                student_obj = Student.objects.get(id = i)
            except:
                raise Exception("Invalid student")
            marks_list.append(Mark(subject_id = subject_id, student_id = student_obj.id, score = int(data[i])))

        marks_obj = Mark.objects.bulk_create(marks_list)
        bundle.obj = subject_obj
        return bundle

    def patch_list(self, request, **kwargs):
        request_user, patch_data = request.user, json.loads(request.body)
        try:
            mark_obj = Mark.objects.get(id = patch_data.get('mark_id'))
        except:
            raise Exception('Mark doesnot exist')
        if not patch_data.get('mark'):
            raise Exception('Please enter marks')
        mark_obj.score = patch_data.get('mark')
        mark_obj.save()
        return HttpResponse(json.dumps({'success':"success"}))