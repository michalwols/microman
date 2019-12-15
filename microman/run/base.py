from typing import Any, Optional
import weakref

from microman import config
from ..time import now, DateTime
from ..status import Status
from ..ids import guid


class Run:
  task: 'task.Task'

  _inputs: Any = None
  _outputs: Any = None

  status: Optional[Status] = None
  error: Optional[BaseException] = None

  meta: dict

  time_created: Optional[DateTime] = None
  time_started: Optional[DateTime] = None
  time_completed: Optional[DateTime] = None

  def __init__(self, task: 'task.Task', id=None, inputs=None):
    self.task = task
    self.id = id or guid()

    self.inputs = inputs

    self.status = Status.SCHEDULED
    self.time_created = now()

  def __repr__(self):
    return f"{self.__class__.__name__}(task={self.task.name}, status={self.status and self.status.value})"

  def __enter__(self):
    self.time_started = now()
    self.status = Status.RUNNING

  def __exit__(self, exception_class, exception, traceback):
    self.time_completed = now()
    if exception:
      self.status = Status.FAILED
      self.error = exception
      return True
    else:
      self.status = Status.COMPLETED

  def __call__(self, *args, **kwargs):
    self.inputs = (args, kwargs)
    with self:
      self.outputs = self.execute(*args, **kwargs)

    return self.outputs

  def execute(self, *args, **kwargs):
    return self.task.func(*args, **kwargs)

  @property
  def inputs(self):
    return self._inputs

  @inputs.setter
  def inputs(self, inputs):
    if config.use_weak_refs:
      try:
        self._inputs = weakref.ref(inputs)
      except TypeError:
        # must have been a type that's not supported by weakref
        self._inputs = inputs
    else:
      self._inputs = inputs

  @property
  def outputs(self):
    return self._outputs

  @outputs.setter
  def outputs(self, outputs):
    if config.use_weak_refs:
      try:
        self._outputs = weakref.ref(outputs)
      except TypeError:
        # must have been a type that's not supported by weakref
        self._outputs = outputs
    else:
      self._outputs = outputs

  @property
  def duration(self):
    return self.time_completed - self.time_started

  @property
  def root(self):
    return './'
