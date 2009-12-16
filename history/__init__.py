# http://stackoverflow.com/questions/420749/how-to-do-text-full-history-in-django

"""
history/__init__.py
"""
from django.core import serializers
from django.utils import simplejson as json
from django.db.models.signals import pre_save, post_save

from history.models import History

def register_history(M):
  """
  Register Django model M for keeping its history

  e.g. register_history(Document) - every time Document is saved,
  its history (i.e. the differences) is saved.
  """
  pre_save.connect(_pre_handler, sender=M)
  post_save.connect(_post_handler, sender=M)

def _pre_handler(signal, sender, instance, **kwargs):
  """
  Save objects that have been changed.
  """
  if not instance.pk:
    return

  # there must be a before, if there's a pk, since
  # this is before the saving of this object.
  before = sender.objects.get(pk=instance.pk)

  _save_history(instance, _serialize(before).get('fields'))

def _post_handler(signal, sender, instance, created, **kwargs):
  """
  Save objects that are being created (otherwise we wouldn't have a pk!)
  """
  if not created:
     return

  _save_history(instance, {})

def _serialize(instance):
   """
   Given a Django model instance, return it as serialized data
   """
   return serializers.serialize("python", [instance])[0]

def _save_history(instance, before):
  """
  Save two serialized objects
  """
  after = _serialize(instance).get('fields',{})

  # All fields.
  fields = set.union(set(before.keys()),set(after.keys()))

  diff = {}

  for field in fields:
    field_before = before.get(field,False)
    field_after = after.get(field,False)

    if field_before != field_after:
        diff[field] = field_before

  history = History(history_for=instance, diff=json.dumps(diff))
  history.save()

