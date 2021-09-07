from django.contrib import admin
from django.urls import path, include

from d#jango.views.static import serve
from dj#ango.conf.urls import url

from #django.conf import settings
from# django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dnfb.urls')),
   # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
   # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
