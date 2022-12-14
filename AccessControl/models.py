from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    SCOUTER = 1
    TUTOR = 2
    RESPONSABLE = 3
    ROLE_CHOICES = (
        (SCOUTER, 'Scouter'),
        (TUTOR, 'Tutor'),
        (RESPONSABLE, 'Responsable'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True, default=1)
    autorizado=models.BooleanField(default=0)
    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
