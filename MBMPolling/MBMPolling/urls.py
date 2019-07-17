from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('voting/',include('voting.urls')),
    path('admin/', admin.site.urls),
]
