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
    path('vendor profile/', views.vendor_profile, name='vendor_profile'),
    path('contact details/', views.contact_details, name='contact_details'),
    path('vendor profile/', views.vendor_profile, name='vendor_profile'),
    path('vendor details/', views.vendor_details ,name='vendor_details'),
    path('sell product/', views.sell_product, name='sell_product'),
    path('product list/', views.product_list, name='product_list'),
    path('product page/<int: pk>', views.product_page, name='product page'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

