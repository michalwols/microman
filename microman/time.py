import signal
import datetime
import functools


class timeout:
  def __init__(self, seconds, message='Timeout'):
    self.seconds = seconds
    self.message = message

  def handle_timeout(self, signum, frame):
    raise TimeoutError(self.message)

  def __enter__(self):
    signal.signal(signal.SIGALRM, self.handle_timeout)
    signal.alarm(self.seconds)

  def __exit__(self, type, value, traceback):
    signal.alarm(0)

  def __call__(self, func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
      with self:
        return func(*args, **kwargs)
    return decorated



now = datetime.datetime.utcnow
delta = datetime.timedelta

DateTime = datetime.datetime