from views import *
from django.conf.urls import include, url

urlpatterns = [
		url(r'^home/$', home, name='home'),
		url(r'^login/', teacher_login, name='teacher_login'),
		url(r'^logout/', teacher_logout, name='teacher_logout'),
		url(r'^assign_marks/', assign_marks, name='assign_marks'),
		url(r'^edit_marks/', edit_marks, name='edit_marks'),
		url(r'^generate_rank/', generate_rank, name='generate_rank'),
		url(r'^add_students_in_bulk/', add_students_in_bulk, name='add_students_in_bulk')
		]