from django.db.models import signals
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import *
from .tasks import send_register_email



@receiver(pre_save,sender=CustomUser)
def display_user(sender,*args, **kwargs):
    print(kwargs)
    return None

@receiver(post_save,sender=CustomUser)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("profile created")
        send_register_email.delay(instance.email)