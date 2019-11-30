from django.shortcuts import render, redirect
from .models import Picture
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def home(request):
    pictures = Picture.objects.all()
    return render(request, 'web/home.html', {"pictures": pictures})


def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'registration/register.html', {"form": form})


def like(request):
    picture_id = request.GET.get('picture_id')
    picture = Picture.objects.get(id=picture_id)
    if request.user.is_authenticated:
        if not request.user in picture.liked_by.all():
            picture.liked_by.add(request.user)
        else:
            picture.liked_by.remove(request.user)
        picture.save()
    return HttpResponse()