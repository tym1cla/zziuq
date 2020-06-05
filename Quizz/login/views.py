from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from .models import Profile
from .forms import *


@login_required
def index(request):
    if 'logout' in request.GET:
        logout(request)
        cache.clear()
        return redirect(login_user)

    user = Profile.objects.all().order_by('-score')

    score = Profile.objects.all().order_by('-score')

    context = {"user": user, "score": score}
    return render(request, 'index.html', context)



def login_user(request):
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = 'Sprawdź poprawność'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            # authenticate user
            user = authenticate(username=username, password=password)
            # handle user authentication
            if user is not None and user.is_active and user.is_authenticated:
                login(request, user)
                return redirect(index)
            else:
                return redirect(login_user)
        else:
            return redirect(login_user)

    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = "Sprawdź poprawność"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = "Hasła różnią się"
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:
                    message = "Użytkownik o takiej nazwie już istnieje！"
                    return render(request, 'register.html', locals())

                same_email_user = User.objects.filter(email=email)
                if same_name_user:
                    message = "Podany mail jest już zarejestrowany！"
                    return render(request, 'register.html', locals())

                # create user and expand user profile
                new_user = User.objects.create_user(username=username, email=email, password=password1)
                user_profile = Profile(user=new_user, sex=sex)
                user_profile.save()

                return redirect(login_user)
        else:
            return render(request, 'register.html', locals())
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


@login_required
def info(request):
    return render(request, 'info.html')
