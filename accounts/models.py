from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_picture = models.ImageField(default = 'default.jpg', upload_to = 'profile_pictures')

    def __str__(self):
        return self.user.username + ' profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.profile_picture.path)

        if image.height > 300 or image.width > 300:
            resized_profile_picture = (300, 300)
            image.thumbnail(resized_profile_picture)
            image.save(self.profile_picture.path)


