from django.shortcuts import render
from .models import WelcomePageOffer, AboutPageInformation



def welcome_page(request):

    offer = WelcomePageOffer.objects.first()

    context = {
	    'offer': offer,
	}

    template_name = 'doit/welcome_page.html'

    return render(request, template_name, context)


def about(request):
    
    offer = AboutPageInformation.objects.first()

    context = {
        'offer': offer,
    }


    template_name = 'doit/about.html'

    return render(request, template_name, context)
