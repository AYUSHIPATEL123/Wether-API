from django.db.models import signals
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(pre_save,sender=CustomUser)
def display_user(sender,*args, **kwargs):
    print(kwargs)
    return None