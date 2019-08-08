from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('demo_app.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]
