from functools import wraps
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse,resolve

def authentication_permission_check(staff_required = None, superuser_required = None):
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated():
                return HttpResponseRedirect(reverse('teacher_login'))
            if not user.is_active:
                return HttpResponseRedirect(reverse('teacher_login'))

            if superuser_required:
                if not user.is_superuser:
                    return HttpResponseRedirect(reverse('teacher_login'))

            return func(request)
        return wraps(func)(inner_decorator)
    return decorator