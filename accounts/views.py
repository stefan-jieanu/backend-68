from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from accounts.forms import SignUpForm
from accounts.models import Profile


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    template_name = 'signup_form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)

        return render(
            request,
            'profile.html',
            context={
                'profile': profile
            }
        )

# Echivalent cu
# @login_required
# def profile_view(request):
#     profile = Profile.objects.get(user=request.user)
#
#     return render(
#         request,
#         'profile.html',
#         context={
#             'profile': profile
#         }
#     )