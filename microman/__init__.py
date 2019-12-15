

from .conf import Config
config = Config(
  use_weak_refs=True,
  default_root='~/microman/',
  default_serializer='json',
  enabled=True
)



from .task import Task, task

from .status import Status
from .params import Param
from .storage import persist
from .files import File
from .background import background

def pipe(*tasks, **named_tasks):
  chain = []
  for t in tasks:
    chain.append(t if isinstance(t, Task) else task(t))
  for name, t in named_tasks.items():
    chain.append(t if isinstance(t, Task) else task(t, name=name))
  return chain
