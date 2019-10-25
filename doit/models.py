from django.db import models
from django.contrib.auth.models import User


class WelcomePageOffer(models.Model):

	title = models.CharField(max_length = 100)
	paragraph = models.TextField()
	pre_offer = models.CharField(max_length = 80)
	button_offer_text = models.CharField(max_length = 40)

	def __str__(self):
		return self.title + ' ---- ' + self.button_offer_text


class AboutPageInformation(models.Model):

    main_title = models.CharField(max_length = 150)
    title_description = models.CharField(max_length = 100, blank = True)
    section_description1 = models.TextField(blank = True)

    title_section2 = models.CharField(max_length = 100, blank = True)
    section2_description = models.TextField(blank = True)

    title_section3 = models.CharField(max_length = 100, blank = True)
    section3_description = models.TextField(blank = True)

    title_section4 = models.CharField(max_length = 100, blank = True)
    section4_description = models.TextField(blank = True)

    def __str__(self):
        return self.main_title


class DoItLine(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    what = models.CharField(max_length = 100, blank = True)
    where = models.CharField(max_length = 50, blank = True)
    when = models.DateTimeField(auto_now_add = True)
    #slug = models.SlugField(default = what)
   

    def __str__(self):
        return str(self.user) + ' ' + self.what

