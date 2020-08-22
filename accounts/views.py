from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string, get_template
from .tokens import account_activation_token
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
import math, random
import uuid
from user_profile.models import *
from .models import *
from cart.models import Cart
from django.contrib import messages
from .forms import SignupForm


# Generate OTP
def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    trans_id = uuid.uuid4().hex[:15]
    return OTP,trans_id

# Verify OTP
def verify_otp(request, trans_id):
    if request.method=="POST":
        otp = request.POST['otp']
        if EmailOTP.objects.filter(trans_id=trans_id, otp=otp).exists():
            return HttpResponseRedirect(reverse('accounts:new_password', kwargs={"trans_id":trans_id}))
        else:
            messages.error(request, "wrong otp")
            return HttpResponseRedirect(reverse('accounts:verify_otp', kwargs={"trans_id":trans_id}))
    return render(request, 'accounts/otp.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['email']
        email = request.POST['email']
        full_name = request.POST['name'].title()
        password = request.POST['password']
        mobile = request.POST['mobile']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return render(request, 'accounts/signup.html')
        if ProfileInfo.objects.filter(mobile=mobile).exists():
            messages.error(request, 'Mobile Number is already registered')
            return render(request, 'accounts/signup.html')
        user = User.objects.create_user(username=email, email=email, password=password, first_name=full_name)
        user.is_active = False
        user.save()
        ProfileInfo.objects.create(user=user, mobile=mobile)
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = render_to_string('email_temp_html.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
        to_email = email
        email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
        email.attach_alternative(message, "text/html")
        email.send()
        messages.success(request, 'Verify your email and login')
        return render(request, 'accounts/login.html')
    return render(request, 'accounts/signup.html')


def activate(request, uidb64, token):
    user = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email Verified successfully')
        return render(request, 'accounts/login.html')
    else:
        return HttpResponse('Activation link is invalid!')


@csrf_protect
def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        user = User.objects.filter(email=email)
        # username = user.username
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Loged in successfully')
            return redirect('products:index')
        elif not User.objects.filter(username=email):
            messages.error(request,'email or mobile is not registered')
            return redirect("accounts:signup")
        elif not User.objects.get(username=email).is_active:
            messages.error(request,'email is not verified')
            return redirect("accounts:login")
        else:
            messages.error(request,' Invalid username or password')
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request,'Loged out successfully')
    return redirect('products:index')

def forgot_password(request):
    if request.method=="POST":
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            otp, trans_id = generate_otp()
            EmailOTP.objects.create(user=user, otp=otp, trans_id=trans_id)
            mail_subject = 'OTP to reset password.'
            message = render_to_string('email_otp.html', {
                        'user': user,
                        'otp':otp,
                    })
            to_email = email
            email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
            email.attach_alternative(message, "text/html")
            email.send()

            return HttpResponseRedirect(reverse('accounts:verify_otp', kwargs={"trans_id":trans_id}))
        else:
            messages.error(request, "user is not registered")
    return render(request, "accounts/forgot_password.html")


def new_password(request, trans_id):
    if request.method=="POST":
        password = request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            user = EmailOTP.objects.get(trans_id=trans_id).user_id
            user = User.objects.get(id=user)
            EmailOTP.objects.get(trans_id=trans_id).delete()
            user.set_password(password)
            user.save()
            messages.success(request, "Password changed succesfully")
            return redirect("accounts:login")
        else:
            messages.error(request, "Passwords must be same")
            return HttpResponseRedirect(reverse('accounts:new_password', kwargs={"trans_id":trans_id}))
    return render(request, 'accounts/new_password.html')


def change_password(request):
    user = request.user
    if request.method=="POST":
        old_password = request.POST['old_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if user.check_password(old_password):
            if password1 == password2:
                user.set_password(password1)
                user.save()
                messages.success(request, "Password changed succesfully")
                return redirect("user_profile:profile")
            else:
                messages.error(request,"Password should be same")
                return redirect("accounts:change_password")
        else:
            messages.error(request,"Old Password is wrong")
            return redirect("accounts:change_password")

    if user.is_authenticated:
        return render(request, 'accounts/change_password.html')
    else:
        return redirect("accounts:login")


def deactivate(request):
    user =request.user
    if request.method=="POST":
        password = request.POST['password']
        if user.check_password(password):
            User.objects.get(id=user.id).delete()
            if Cart.objects.filter(user_id=user.id).exists():
                Cart.objects.filter(user_id=user.id).delete()
            if ProfileInfo.objects.filter(user_id=user.id).exists():
                ProfileInfo.objects.get(user_id=user.id).delete()
            if Address.objects.filter(user_id=user.id).exists():
                Address.objects.filter(user_id=user.id).delete()
            if Card.objects.filter(user_id=user.id).exists():
                Card.objects.filter(user_id=user.id).delete()
            messages.success(request, "account deactivated")
            return redirect("products:index")
        else:
            messages.error(request, "wrong password")
            return redirect("accounts:deactivate")
    if user.is_authenticated:
        return render(request, 'accounts/deactivate.html')
    else:
        return redirect("accounts:login")


def signup1(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            mobile = form.cleaned_data.get('mobile')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # check email is already registered or not
            if User.objects.filter(email=email).exists():
                messages.error(request, "user already registed with this email {}".format(email))
                return render(request,"accounts/signup1.html", context={"form": form})

            # check mobile number is already registered or not
            if ProfileInfo.objects.filter(mobile=mobile).exists():
                messages.error(request, "user already registed with this number {}".format(mobile))
                return render(request,"accounts/signup1.html", context={"form": form})

            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            user.is_active = False
            user.save()
            ProfileInfo.objects.create(user=user, mobile=mobile)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('email_temp_html.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
            to_email = email
            email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
            email.attach_alternative(message, "text/html")
            email.send()
            messages.success(request, 'Verify your email and login')
            return render(request, 'accounts/login.html')

    form = SignupForm()
    return render(request, 'accounts/signup1.html', context={'form':form})