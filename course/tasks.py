from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def notification_of_changes(course, subscribers_email: list | tuple):
    message = f"There are new changes in the {course} course. Come and see what's new in it"
    send_mail(
        subject=f'Update in course {course}',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=subscribers_email
    )
