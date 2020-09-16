from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *



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
            form = AddressForm(request.POST)
            if form.is_valid():
                address = Address.objects
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                mobile = form.cleaned_data.get('mobile')
                locality = form.cleaned_data.get('locality')
                area = form.cleaned_data.get('area')
                town = form.cleaned_data.get('town')
                pin = form.cleaned_data.get('pin')
                landmark = form.cleaned_data.get('landmark')
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

    user = request.user
    if not user.is_authenticated:
        return redirect("accounts:login") 
    user_info = User.objects.get(id=user.id)
    profile_info = ProfileInfo.objects.get(user=user)
    addresses = Address.objects.filter(user=user)
    cards = Card.objects.filter(user=user)
    form = AddressForm()
    context = {
                "user_info":user_info,
                "profile_info":profile_info,
                "addresses":addresses,
                "cards":cards,
                "form":form,
            }
    return render(request, 'profile/my_profile.html', context)


def del_card(request, id):
    # user = requesst.user
    card = Card.objects.get(id=id)
    card.delete()
    return redirect("user_profile:profile")


def del_addr(request, id):
    # user = requesst.user
    addr = Address.objects.get(id=id)
    addr.delete()
    return redirect("user_profile:profile")


def edit_addr(request, id):
    # user = requesst.user
    addr = Address.objects.get(id=id)
    return redirect("user_profile:profile", {'addr':addr})
