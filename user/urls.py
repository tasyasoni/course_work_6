from django.urls import path
from user.apps import UsersConfig
from user.views import LoginView, LogoutView, RegisterView, ProfileView, activate, email_activate, restore_password

app_name = UsersConfig.name


urlpatterns = [
    path('user/login/', LoginView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(), name='logout'),
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/profile/', ProfileView.as_view(), name='profile'),
    path('user/activate/<str:uid>/', activate, name="activate"),
    path('user/email_activate/', email_activate, name="email_activate"),
    path('user/restore_password/', restore_password, name="restore_password"),
]