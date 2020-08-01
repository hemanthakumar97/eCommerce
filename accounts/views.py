from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string, get_template
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
# from account.models import *
import math, random 
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        username = request.POST['email']
        full_name = request.POST['full_name'].title()
        email = request.POST['email']
        password = request.POST['password']
        # mobile = request.POST['mobile']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return render(request, 'accounts/signup.html')
        # if User.objects.filter(mobile=mobile).exists():
        #     messages.error(request, 'Mobile Number is already registered')
            return render(request, 'accounts/signup.html')
        user = User.objects.create_user(username=email, email=email, password=password, first_name=full_name)
        user.is_active = False
        user.save()
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
        messages.success(request, 'Registered succesfully')
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
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
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
            return redirect('products:index')
        else:
            messages.error(request,' Invalid username or password')
            return render(request,'accounts/login.html')
    return render(request, 'accounts/login.html')


def logout(request):
        auth.logout(request)
        return redirect('products:index')

def forgot_password(request):
    return render(request, "accounts/forgot_password.html")