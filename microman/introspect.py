import inspect
from inspect import signature, getsource, getsourcefile


from contextvars import ContextVar
from contextlib import contextmanager

from functools import wraps

caller = ContextVar('caller')


# @contextmanager
# def track():
#     t = caller.set()
#     yield
#     caller.reset(t)


def trace(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    print('calling from', caller.get())
    token = caller.set(f)

    print('into', caller.get())
    r = f(*args, **kwargs)
    caller.reset(token)
    return r
  return decorated
