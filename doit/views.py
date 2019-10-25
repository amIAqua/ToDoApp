from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import PlanLineAdd
from .models import (WelcomePageOffer,
                     AboutPageInformation,
                     DoItLine)


class WelcomePageView(View):

    template_name = 'doit/welcome_page.html'

    def get(self, request, *args, **kwargs):
    
        offer = WelcomePageOffer.objects.first()
        context = {
	        'offer': offer,
	        }   
        return render(request, self.template_name, context)


class MainUserScreenTable(View):

    template_name = 'doit/main_user_screen.html'

    def get(self, request, *args, **kwargs):

        table = DoItLine.objects.filter(user = request.user).order_by('-id')
        add_line_form = PlanLineAdd()
        context = {
            'table': table,
            'add_line_form': add_line_form, 
            }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        add_line_form = PlanLineAdd(request.POST)
        if add_line_form.is_valid():
            line = add_line_form.save(commit=False)
            line.user = request.user
            line.save()
            return redirect(reverse_lazy('doit:plans'))


def delete_table_line(request, id):

    obj = DoItLine.objects.filter(id = id)
    obj.delete()
    return redirect(reverse_lazy('doit:plans'))

def edit_table_line(request, id):

    obj = get_object_or_404(DoItLine, id = id)
    add_line_form = PlanLineAdd(instance = obj)

    if request.method == 'POST':
        add_line_form = PlanLineAdd(request.POST, instance = obj)
        if add_line_form.is_valid():
            add_line_form.save() 
            return redirect(reverse_lazy('doit:plans'))
    
def about(request):
    
    offer = AboutPageInformation.objects.first()
    context = {
        'offer': offer,
    }
    template_name = 'doit/about.html'
    return render(request, template_name, context)
