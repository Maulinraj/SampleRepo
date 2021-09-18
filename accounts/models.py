from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.IntegerField(default=0)
    update_last = models.DateTimeField(default='2012-09-04 06:00:00.000000-08:00')

    def __str__(self):  
          return self.user.username

    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Repositories(models.Model):
    repo_name = models.CharField(max_length=100)
    username = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.repo_name
