from uuid import uuid4


def sluggify(text):
  text = text.strip().lower()
  return '-'.join(text.split())


guid = uuid4

__all__ = ['sluggify', 'guid']
