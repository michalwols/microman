from typing import Union, Callable
from ..run import Run, AsyncRun



class Runner:
  Run: Run = Run

  def __call__(self, run: Union['Task', Run, Callable], *args, **kwargs):
    from ..task import Task
    if isinstance(run, Task):
      run = self.Run(task=run)
    run(*args, **kwargs)

    return run




class AsyncRunner(Runner):
  Run: AsyncRun = AsyncRun

  async def __call__(self, run: Union['Task', Run, Callable], *args, **kwargs):
    from ..task import Task
    if isinstance(run, Task):
      run = self.Run(task=run)

    await run(*args, **kwargs)

    return run