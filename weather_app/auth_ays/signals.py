from django.db.models import signals
from django.db.models.signals import pre_save,post_save,post_delete,pre_delete,m2m_changed,pre_migrate,post_migrate,pre_init,post_init 
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


@receiver(post_delete,sender=Profile)
def delete_profile(sender,instance,**kwargs):
    if instance.profile_image:
        instance.profile_image.delete(save=False)
        print("profile image deleted")

