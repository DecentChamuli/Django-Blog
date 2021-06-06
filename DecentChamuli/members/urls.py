from django.urls import path, include
from .views import CreateProfilePageView, UserRegisterView, EditProfilePageView, UserEditView, PasswordsChangeView, ShowProfilePageView
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('profile/edit', UserEditView.as_view(), name='edit_profile'),
    path('account/edit', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password-updated', views.password_success, name="password_success"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('profile/edit/<int:pk>', EditProfilePageView.as_view(), name="edit_profile_page"),
    path('profile/create', CreateProfilePageView.as_view(), name="create_profile_page"),
    
]