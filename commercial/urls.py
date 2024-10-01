from django.urls import path
from commercial import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('shop/',views.shop, name='shop'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('why/', views.why, name='why'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout,name='logout'),
    path('manage/', views.manage, name='manage'),
    path('manage/register/',views.register, name='register'),
    path('user profile/', views.user_profile, name='user_profile'),
    path('profile success/', views.profile_success, name='profile_success'),
    #path('vendor_profile_setup/', views.vendor_profile_setup, name='vendor_profile_setup'),
    path('vendor_profile/', views.vendor_profile, name='vendor_profile'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

