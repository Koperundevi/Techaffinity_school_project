from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import include, url, handler400, handler500
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.i18n import JavaScriptCatalog
from api.tools import v1_api
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^school/', include('web.urls'), name='school'),
    url(r'^api/', include(v1_api.urls)),
]
