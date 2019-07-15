Developer - Koperundevi A

1. Required software packages

Django==1.10.0
django-tastypie==0.13.3  
django_pandas
numpy

2. Using the below command install the above software packages one by one if not installed already.

pip install 'package-name'

3. from the location /schoolsite/ run the below commands to create the required models.

python manage.py makemigrations web
python manage.py migrate

4. Run the application using below command from the location /schoolsite/

python manage.py runserver 0.0.0.0:8000


Note:

To create users, subjects and student using the admin portal - http://localhost:8000/admin
To assign, edit marks and generate ranks using the app portal - http://localhost:8000/school/login/


