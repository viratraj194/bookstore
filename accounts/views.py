from django.shortcuts import get_object_or_404, render,redirect
from accounts.forms import UserForm, UserInfoForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_decode
from django.contrib import  auth
from django.contrib.auth.tokens import default_token_generator
from django.template.defaultfilters import slugify
from accounts.models import User, UserProfile
from accounts.utils import send_verification_email


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
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.slug = slugify(first_name) + '-' + str(user.id)
            user.save()

            # send email verification
            mail_subject = 'please activate your account'.title()
            mail_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, mail_template)

            return redirect('home')
        else:
            print(form.errors)   
    else: 
        form = UserForm

    context = {
        'form':form

    }
    return render(request,'accounts/registerUser.html',context)


def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        print('account is active now')
        return redirect('account')
    else:
        print('invalid activation link')
        return redirect('account')

        



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


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact = email)
            mail_subject = 'please click below link to reset password'.title()
            mail_template = 'accounts/emails/reset_password_email.html'
            send_verification_email(request, user, mail_subject, mail_template)
            return redirect('login')
        else:
            return redirect('forgot_password')
    return render(request,'accounts/forgot_password.html')


def reset_password_validate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid) 
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid
        return redirect('reset_password')
    else:
        return redirect('account')



def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        conform_password = request.POST['conform_password']
        if password == conform_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return redirect('reset_password')
    return render(request, 'accounts/reset_password.html')

    