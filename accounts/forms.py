from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True, label="First Name", widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=20, required=True,  label="Last Name", widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}))
    mobile = forms.CharField(max_length=20, required=False, label="Mobile Number", widget=forms.TextInput(attrs={'placeholder':'Mobile Number', 'pattern':'[6-9]\d{9}'}))
    # gender = forms.ChoiceField(choices=[("Male", "Male"), ("Femal","Female")], required=False, widget=forms.RadioSelect)
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
