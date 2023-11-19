from django.contrib import admin
from django.urls import path,include
from teacher.api.views import StudentRegisterview

urlpatterns = [
    path('register', StudentRegisterview.as_view())
]