from django.contrib import admin

from models import *

admin.site.site_url = '/school/home'
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Mark)