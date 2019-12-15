from .base import Runner


_default_runner = Runner()


def default(val=None):
  global _default_runner
  if val:
    _default_runner = val
  return _default_runner