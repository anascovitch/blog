# """
# URL configuration for monprojet project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views
# from monapp.views import register,upload_image,user_profile, edit_profile, edit_post, post_detail,delete_post,delete_post_confirm,profile_redirect


# app_name='monapp'
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register/',register, name='register'),
#     path('upload_image/',upload_image, name='upload_image'),
#     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#     path('password-change/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='password_change'),
#     path('profile/<str:username>/', user_profile, name='user_profile'),
#     path('edit_profile/', edit_profile, name='edit_profile'),
#     path('post/edit/<int:post_id>/', edit_post, name='edit_post'),
#     path('post/<int:post_id>/', post_detail, name='post_detail'),
#     path('post/<int:post_id>/delete/confirm/', delete_post_confirm, name='delete_post_confirm'),
#     path('post/<int:post_id>/delete/',delete_post, name='delete_post'),
#     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#     path('accounts/profile/', profile_redirect, name='profile_redirect'),
# ]
# monapp/urls.py

from django.urls import path
from . import views
from .views import login_redirect, profile_view, CustomPasswordChangeView, custom_logout #, CustomPasswordResetView,CustomPasswordResetConfirmView
from . import views


app_name = 'monapp'

urlpatterns = [
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('accounts/profile/', views.profile_redirect, name='profile_redirect'),
    path('login/redirect/', login_redirect, name='login_redirect'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('logout/', custom_logout, name='logout'),
    # path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # path('accounts/reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   
]



