from django.contrib import admin
from .models import Products
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin
from .models import VendorProfile
from .models import UserProfile

admin.site.register(Products)
admin.site.register(UserProfile)
admin.site.register(VendorProfile)

class CustomGroupAdmin(GroupAdmin):
    def users_in_group(self, obj):
        return ", ".join([user.username for user in obj.user_set.all()])
    
    users_in_group.short_description = 'Users'

    list_display = ('name', 'users_in_group')
    admin.site.unregister(Group)

admin.site.register(Group, CustomGroupAdmin)