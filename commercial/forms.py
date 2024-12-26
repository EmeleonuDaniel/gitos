from .models import VendorProfile,UserProfile,Product
from django import forms


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['profile_picture'].widget.attrs.update({'class': 'form-control'})

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = ['brand_picture']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image1','image2','image3','image4','image5','image6',]


