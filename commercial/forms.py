from .models import VendorProfile
from django import forms


class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = ['user','profile_picture','seller_profile','brand_name','WA_link']



