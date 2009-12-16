# http://stackoverflow.com/questions/420749/how-to-do-text-full-history-in-django
"""
history/models.py
"""

from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class History(models.Model):
  """
     Retain the history of generic objects, e.g. documents, people, etc..
  """

  content_type = models.ForeignKey(ContentType, null=True)

  object_id = models.PositiveIntegerField(null=True)

  history_for = generic.GenericForeignKey('content_type', 'object_id')

  diff = models.TextField()

def __unicode__(self):
  return "<History (%s:%d):%d>" % (self.content_type, self. object_id, self.pk)

