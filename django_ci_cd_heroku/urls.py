from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('names.urls')),
    path('', RedirectView.as_view(url='show/')),
]
