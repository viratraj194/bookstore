from django.shortcuts import get_object_or_404, render,redirect
from accounts.forms import UserForm, UserInfoForm, UserProfileForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import  auth

from accounts.models import UserProfile


@login_required(login_url='login')
def account(request):
    user = request.user
  
    if user.is_superadmin:
       return redirect('/admin')
    else :
        return redirect('dashboard')
    


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect('home')
        else:
            print(form.errors)   
    else: 
        form = UserForm

    context = {
        'form':form

    }
    return render(request,'accounts/registerUser.html',context)



def login(request):
    if request.user.is_authenticated:
        return redirect('account')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request,user)
            print('success')
            return redirect('account')
        else:
            print('error')
    return render(request,'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')

@login_required(login_url='login')
def profile_settings(request):
    profile = get_object_or_404(UserProfile,user=request.user)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES,instance=profile)
        user_form = UserInfoForm(request.POST,instance=request.user)
        if profile_form and user_form.is_valid():
            profile_form.save()
            user_form.save()
            # messages.success(request,'profile has been updated'.title())
            return redirect('dashboard')
        else:
            print(profile_form.errors)
            print(user_form.errors)
    else:
        profile_form = UserProfileForm(instance=profile)
        user_form = UserInfoForm(instance=request.user)

    context = {
        'profile_form':profile_form,
        'user_form':user_form,
        'profile':profile
    }

    return render(request,'accounts/profile_settings.html',context)