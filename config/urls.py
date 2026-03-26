from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Welcome to Simple LMS")

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
]