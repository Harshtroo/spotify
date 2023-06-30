from django.dispatch import receiver
from .models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import threading

class EmailThreading(threading.Thread):
    def __init__(self,email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        self.email.send(fail_silently=False)

@receiver(post_save, sender=User)
def send_user_email(sender, instance, created, **kwargs):
    if created:
        email_subject = "Registration confirmation"
        email_body = render_to_string("email_template.html", {'context': instance.username, })
        email = EmailMessage(email_subject,
                  email_body,
                  settings.EMAIL_HOST_USER,[instance.email])
        email.content_subtype = 'html'
        # email.send()
        EmailThreading(email).start()
