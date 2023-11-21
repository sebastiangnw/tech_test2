""" Urls """

from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from comments import views


router = routers.DefaultRouter()
router.register(r"", views.CommentViewSet)

urlpatterns = [
    path("api/", include(router.urls), name="Api_comments"),
    path("docs/", include_docs_urls(title="Comments API"), name="docs"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='comments/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
