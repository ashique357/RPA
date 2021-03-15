from django.urls import path

from . import views

urlpatterns = [
    path('file-manipulation/',views.file_manipulation),
]