"""
URL configuration for bigquery project.

"""
from django.contrib import admin
from django.urls import path, include
from comments import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.frontpage, name="frontpage"),
    path("comments/", include("comments.urls")),
    path('rooms/', include('room.urls')),
    path("graphics/", include("graphics.urls")),
]
