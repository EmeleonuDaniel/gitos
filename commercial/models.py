from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
    user = models.OneToOneField(User, db_index=True,on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50,null=True, blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True,null=True,default='profile_pictures/default user.png')
    email = models.EmailField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

#used django signals to make sure a User profile is created when a user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Products(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()
    
    def __str__(self):
        return self.name

class VendorProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    DOB = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10, default=None,null=True,blank=True)
    address = models.TextField(default=None,null=True,blank=True)
    phone = models.CharField(max_length=15,default=None,null=True,blank=True)
    package = models.CharField(max_length=100,default=None,null=True,blank=True)
    brand_name = models.CharField(max_length=255,default=None,null=True,blank=True)
    WA_link = models.URLField(max_length=200,default=None,null=True,blank=True)
    brand_picture = models.ImageField(upload_to='brand_images/',null=True,blank=True,default='brand_images/default.jpg')


    
    


