from .models import VendorProfile
from django import forms
from .models import UserProfile

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = ['user','brand_picture','brand_name','WA_link']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']



