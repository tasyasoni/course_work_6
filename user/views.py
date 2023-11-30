import random
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from user.forms import UserRegisterForm, UserProfileForm
from user.models import User


class LoginView(BaseLoginView):
    model = User
    template_name = 'user/login.html'
    # success_url = reverse_lazy('mainapp:home')

class LogoutView(BaseLogoutView):
    model = User
    # success_url = reverse_lazy('mainapp:home')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        verification = gen_verify_code()
        new_user.email_verify = verification
        new_user.is_active = False  #делаем нового юзера неактивным
        verification_url = f'http://127.0.0.1:8000/user/activate/{verification}'
        send_mail(
            subject='Подтверждение адреса электронной почты',
            message=f'Для подтверждения вашей почты перейдите по ссылке: {verification_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        new_user.save()

        return super().form_valid(form)


class ProfileView (UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/profile.html'
    success_url = reverse_lazy('mailier:home')

    def get_object(self, queryset=None):
        return self.request.user


def email_activate(request):
    return render(request, "user/email_activate.html")


def activate(request, uid):
    user = User.objects.filter(email_verify=int(uid)).first()
    user.is_active = True
    user.save()
    return redirect(reverse('mailier:home'))


def restore_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        new_password = gen_verify_code()
        send_mail(
            subject='Восстановление пароля',
            message=f'Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse('user:login'))
    return render(request, "user/restore_password.html")


def gen_verify_code():
   return (''.join([str(random.randint(0, 9)) for i in range(4)]))
