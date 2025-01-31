from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm, CustomLoginForm, CustomPasswordChangeForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordResetView
from .forms import ProfilePhotoForm


def update_profile_photo(request):
    if request.method == 'POST':
        form = ProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile photo updated successfully!')
            return redirect('accounts:dashboard_view')  # Replace 'profile' with your profile page URL name
    else:
        form = ProfilePhotoForm(instance=request.user)

    return render(request, 'accounts/update_profile_photo.html', {'form': form})

def login_view(request):
    # If the user is authenticated, redirect to home page
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('home')  # Ensure this is the correct name for your home page

    # Handle form submission
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Authenticate user
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                request.session.modified = True
                messages.success(request, 'Login successful!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = CustomLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    # If the user is authenticated, redirect to home page
    if request.user.is_authenticated:
        messages.info(request, 'You are already registered and logged in.')
        return redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('accounts:login_view')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'templates/registration/password_reset_email.html'

@login_required
def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login_view') 
    
    return render(request, 'accounts/dashboard.html')

# @login_required
# def dashboard_view(request):
    
#     # Check the user's role
#     if request.user.role == 'patient':
#         return render(request, 'accounts/patient_dashboard.html')
#     elif request.user.role == 'doctor':
#         return render(request, 'accounts/doctor_dashboard.html')
#     else:
#         # Redirect or handle unknown roles
#         return redirect('error_page')  # Replace 'error_page' with your actual error page


@login_required
def profile_update_view(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('accounts:dashboard_view')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, 'accounts/profile_update.html', {'form': form})


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevents logout after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'accounts/change_password.html', {'form': form})
















def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('accounts:login_view')



