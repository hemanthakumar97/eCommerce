from django import forms

class AddressForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True, label=False, widget=forms.TextInput(attrs={'placeholder':'First Name', 'id':'pi'}))
    last_name = forms.CharField(max_length=20, required=False,  label=False, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'id':'pi'}))
    mobile = forms.CharField(max_length=20, required=True, label=False, widget=forms.TextInput(attrs={'placeholder':'Mobile Number', 'pattern':'[6-9]\d{9}', 'id':'pi'}))
    locality = forms.CharField(max_length=20, required=False, label=False, widget=forms.TextInput(attrs={'placeholder':'Locality', 'id':'pi'}))
    area = forms.CharField(max_length=50, required=True, label=False, widget=forms.Textarea(attrs={'placeholder':'Address (Area and Street)', 'id':'pi'}))
    town = forms.CharField(max_length=20, required=True, label=False, widget=forms.TextInput(attrs={'placeholder':'City/Town'}))
    pin = forms.CharField(max_length=20, required=True, label=False, widget=forms.TextInput(attrs={'placeholder':'Pincode','pattern':'\d{6}'}))
    landmark = forms.CharField(max_length=20, required=False, label=False, widget=forms.TextInput(attrs={'placeholder':'Landmark', 'id':'pi'}))

    
