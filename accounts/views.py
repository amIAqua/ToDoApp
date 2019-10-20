from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

def join(request):

    template_name = 'accounts/join.html'

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! Now Log in!')
            return redirect('accounts:login')
    
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, template_name, context)

def profile(request):

    template_name = 'accounts/profile.html'

    return render(request, template_name)