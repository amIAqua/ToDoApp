from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import View
from .forms import (UserRegistrationForm,
                    UserUpdateForm,
                    UserProfileUpdateForm)


class JoinView(View):

    template_name = 'accounts/join.html'

    def get(self, request, *args, **kwargs):

        registration_form = UserRegistrationForm()
        context = {
            'registration_form': registration_form
            }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            first_name = registration_form.cleaned_data.get('first_name')
            last_name = registration_form.cleaned_data.get('last_name')
            email = registration_form.cleaned_data.get('email')
            username = registration_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now Log in!')
            return redirect(reverse('login'))
        
    
class ProfileView(View):

    def get(self, request):
        return render(request, 'accounts/profile.html')


class ProfileUpdateView(View):

    template_name = 'accounts/update_profile.html'

    def get(self, request, *args, **kwargs):

        self.u_form = UserUpdateForm(instance = request.user)
        self.p_form = UserProfileUpdateForm(instance = request.user.userprofile)

        context = {
            'u_form': self.u_form,
            'p_form': self.p_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        self.u_form = UserUpdateForm(request.POST, instance = request.user )
        self.p_form = UserProfileUpdateForm(request.POST, request.FILES, instance = request.user.userprofile)

        if self.u_form.is_valid():
            if self.p_form.is_valid():
                self.u_form.save()
                self.p_form.save()
                messages.success(request, f"Profile has been successfully updated!")
                return redirect('profile')


