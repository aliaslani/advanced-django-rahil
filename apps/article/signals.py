from django.db.models.signals import post_save
from django.core.signals import request_started, request_finished

from django.dispatch import receiver
from apps.article.models import Article
from django.core.mail import send_mail


@receiver(post_save, sender=Article)
def send_thankfull_message(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Thankful Article',
            message = kwargs.get('message'),
            from_email='myemail@gmail.com',
            recipient_list=[instance.author.email],

        )
