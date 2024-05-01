from celery import shared_task
from datetime import datetime, timedelta
from users.models import User

ABSENSE_PERIOD = 30


@shared_task
def deactivate_users():
    today = datetime.now().date()
    active_users = User.objects.filter(is_active=True)
    for user in active_users:
        if user.last_login and (today - user.last_login.date()) > timedelta(days=ABSENSE_PERIOD):
            user.is_active = False
            user.save()
