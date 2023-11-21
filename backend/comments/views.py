"""This file contains the views for the tasks app."""

from django.shortcuts import render, redirect
from django.contrib.auth import login
from rest_framework import viewsets
from .serializer import CommentSerializer
from .models import Comment
from .forms import SignUpForm

# Create your views here.


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for Comment model."""
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


def frontpage(request):
    """Frontpage view."""
    return render(request, 'comments/frontpage.html')


def signup(request):
    """Signup view."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'comments/signup.html', {'form': form})
