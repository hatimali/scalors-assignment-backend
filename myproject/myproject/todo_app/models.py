from __future__ import unicode_literals

from django.db import models
from .tasks import execute_reminder


class Board(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)


class TODO(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField()

    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='todos')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.title)


class Reminder(models.Model):
    post_url = models.URLField()
    text = models.TextField()
    delay = models.IntegerField()

    def __unicode__(self):
        return unicode(self.post_url)

    def save(self, *args, **kwargs):
        super(Reminder, self).save(*args, **kwargs)
        if self.delay:
            seconds = self.delay * 60
            execute_reminder.apply_async((self.pk,), countdown=seconds)
            pass
