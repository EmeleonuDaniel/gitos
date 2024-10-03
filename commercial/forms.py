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

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['profile_picture'].widget.attrs.update({'class': 'form-control'})



