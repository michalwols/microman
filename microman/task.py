from .run import Run
from .time import DateTime
from .types import GUID
from .ids import sluggify
from . import runners
from . import config


class Task:
  id: GUID
  name: str
  description: str

  time_created: DateTime = None
  scheduled_start_time: DateTime

  retries = 0
  retry_policy = None

  params: dict

  root = None
  parent = None
  children = []

  runner = None
  track_runs = True
  runs: list

  enabled = True  # flag to opt out of tracking and run the func as if it wasn't decorated

  def __init__(
    self,
    func,
    name=None,
    description=None,
    slug=None,
    *args,
    **kwargs
  ):
    self.func = func

    self.name = name
    self.description = description
    self.slug = slug or sluggify(name)

    self.runs = []

  def __call__(self, *args, **kwargs):
    if not self.enabled:
      return self.func(*args, **kwargs)

    if self.retries:
      for attempt in range(self.retries):
        run = self.run(*args, **kwargs)
        if not run.error:
          return run.outputs
        # FIXME: raise run.error here?
        raise run.error
    else:
      run = self.run(*args, **kwargs)
      return run.outputs

  def run(self, *args, **kwargs):
    runner: 'runners.Runner' = self.runner or runners.default()
    run = runner(self, *args, **kwargs)
    if self.track_runs:
      self.runs.append(run)
    return run

  def map(self):
    pass

  def schedule(self):
    pass

  @classmethod
  def from_function(cls, f):
    pass

  def expose(self):
    pass

  def hook(self):
    pass

  def on_error(self):
    pass

  def before(self):
    pass

  def then(self):
    pass

  def local_root(self):
    pass

  def log(self):
    pass

  def subtask(self, f, *args, **kwargs):
    return Task(f)

  def backfill(self):
    pass

  def save(self):
    pass


def task(func=None, name=None, description=None, **kwargs):
  if not config.enabled:
    return func

  if callable(func):
    return Task(
      func=func,
      name=name or func.__name__,
      description=description or func.__doc__
    )
  else:
    def decorator(func):
      return Task(
        func=func,
        name=name or func.__name__,
        description=description or func.__doc__
      )

    return decorator



class AyncTask(Task):
  """
  Support async functions
  """
  pass


class StaticTask(Task):
  """
  Allow airflow style graph definition
  """
  pass