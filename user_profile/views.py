from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages



def my_profile(request):
    if request.method=="POST":
        user=request.user
        if "pers_info" in request.POST:
            user_profile = ProfileInfo.objects.filter(user=user)
            first_name = request.POST['first_name'].title()
            last_name = request.POST['last_name'].title()
            mobile = request.POST['mobile']
            if not ProfileInfo.objects.get(user=user).gender:
                gender = request.POST['gender']
                user_profile.update(gender=gender)
            if  ProfileInfo.objects.get(user=user).mobile != int(mobile) and ProfileInfo.objects.filter(mobile=mobile).exists():
                messages.error(request,"Mobile Number is already registered")
                return redirect("user_profile:profile")
            else:
                user_profile.update(mobile=mobile)
                messages.success(request,"Updated succesfully")
            User.objects.filter(id=user.id).update(first_name=first_name,last_name=last_name)
            return redirect("user_profile:profile")

        if "address" in request.POST:
            address = Address.objects
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            mobile = request.POST['mobile']
            locality = request.POST['locality']
            area = request.POST['area']
            town = request.POST['town']
            pin = request.POST['pin']
            landmark = request.POST['landmark']
            try:
                address.create(user=user, first_name=first_name, last_name=last_name, mobile=mobile,
                locality=locality, area=area, city=town, pin=pin, landmark=landmark)
                messages.success(request,"Address added succesfully")
            except:
                messages.error(request,"Something is wrong")
            return redirect("user_profile:profile")

        if "add_card" in request.POST:
            card = Card.objects
            card_no = request.POST['card_no']
            expiry_month = request.POST['exp_month']
            expiry_year = request.POST['exp_year']
            cvv = request.POST['cvv']
            name = request.POST['name_on_card']
            try:
                card.create(user=user, card_no=card_no, expiry_month=expiry_month,expiry_year=expiry_year,
                            cvv=cvv,name=name)
                messages.success(request,"Card added succesfully")
            except:
                messages.error(request,"Something is wrong")
            return redirect("user_profile:profile")

        
    user_info = User.objects.get(id=request.user.id)
    profile_info = ProfileInfo.objects.get(user=request.user)
    addresses = Address.objects.filter(user=request.user)
    cards = Card.objects.filter(user=request.user)
    context = {
                "user_info":user_info,
                "profile_info":profile_info,
                "addresses":addresses,
                "cards":cards,
            }
    return render(request, 'profile/my_profile.html', context)
