import requests
from celery import shared_task


@shared_task
def execute_reminder(reminder_id):
    from .models import Reminder
    try:
        reminder = Reminder.objects.get(pk=reminder_id)
    except Reminder.DoesNotExist:
        return 'reminder removed success'

    from .serializers import ReminderSimpleSerializer
    post_url = reminder.post_url
    data = ReminderSimpleSerializer(reminder).data
    try:
        response = requests.post(post_url, data=data)
        response.raise_for_status()
    except Exception as e:
        # some retry logic
        return e.message

    reminder.delete()  # should we do this?
    return 'success'
