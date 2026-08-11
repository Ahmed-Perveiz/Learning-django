from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # make one to one relation with users model 1:1
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


