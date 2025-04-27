from django.shortcuts import render, redirect
from . import forms
from car.models import Car
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages


# Create your views here.

@login_required
def profile(request):
    bought_cars = Car.objects.filter(buyer=request.user)
    listed_cars = Car.objects.filter(author=request.user)

    return render(request, 'profile.html', {'bought_cars': bought_cars, 'listed_cars': listed_cars})


def signup(request):
    if not request.user.is_authenticated:
        form = forms.RegisterForm()
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
                return redirect('login')
            else:
                errors = []
                for field, field_errors in form.errors.items():
                    for error in field_errors:
                        errors.append(f"{error}")
                messages.error(request, " ".join(errors))
        else:
            form = forms.RegisterForm()
        return render(request, 'signup.html')
    else:
        return redirect('home')


def user_login(request):
    if not request.user.is_authenticated:
        next_url = request.GET.get('next', 'home')
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST) 
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully')
                    return redirect(next_url)
                else:
                    messages.error(request, 'Invalid username or password')            
            else:
                errors = []
                for field, field_errors in form.errors.items():
                    for error in field_errors:
                        errors.append(f"{error}")
                messages.error(request, " ".join(errors))
        else:
            form = AuthenticationForm()
        return render(request, 'signin.html')
    else:
        return redirect('home')


def user_logout(request):
    logout(request)
    messages.info(request, "Logged Out Successfully")
    return redirect('home')


@login_required
def password_change(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль було успішно оновлено!')
            return redirect('edit_profile')
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f"{error}")
            messages.error(request, " ".join(errors))
    return render(request, 'password_change.html', {'form': form})
    

@login_required
def edit_profile(request):    
    edit_profile_form = forms.EditProfileForm(instance=request.user)
    if request.method == 'POST':
        edit_profile_form = forms.EditProfileForm(request.POST, instance=request.user)
        if edit_profile_form.is_valid():
            messages.success(
                request, 'Your user data was successfully updated.')
            edit_profile_form.save()
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        edit_profile_form = forms.EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': edit_profile_form})