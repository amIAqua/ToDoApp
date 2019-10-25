from django.contrib import admin
from .models import (WelcomePageOffer,
                     AboutPageInformation,
                     DoItLine,
                    )



admin.site.register(WelcomePageOffer)
admin.site.register(AboutPageInformation)
admin.site.register(DoItLine)
