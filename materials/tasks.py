from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def send_course_update(course_id, subject, message, recipient_list):
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
