from celery import shared_task
import time
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_register_email(email):
    print("starting the email sending task")
    
    send_mail(
        subject='Welcome to Weather App',
        message='<h1>Thank you for registering to our weather app. We hope you have a great experience using our app.</h1>',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email,],
        html_message='<h1>Thank you for registering to our weather app. We hope you have a great experience using our app.</h1>',
        fail_silently=False,
    )
    return "done"

