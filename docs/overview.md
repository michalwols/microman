


# Task

A task describes a function to be performed. It can call into other tasks to define computation graphs.
Unlike a typical workflow scheduler there is no need to define a static "DAG", 
instead the computation is defined by run, allowing you to branch, recurse and bail out at any point 
like any other python function.

```python
from microman import task, persist

@task
def get_stripe_sales():
   pass

@task
def get_firebase_stats():
   pass

@task
@persist(outputs='gcs://bucket/{scheduled_time}/report.csv')
def generate_report(scheduled_time):
  sales = get_stripe_sales()
  stats = get_firebase_stats()
  
  return sales.join(stats, 'account_id')

generate_report()  # run the task
```

Turning a function into a task with the `@task` decorator enables execution tracking, retries and many other features that are mentioned in this guide.
 

# Task Run 

An execution of a task is called a `Run`. It tracks the inputs and outputs to the task as well as the time of execution and errors.

```python
last_run = generate_report.runs[-1]


```

# Task Runners

A runner handles executing run in different environments. By default runs are executed in the main process. 

```python
from microman.runners.dask import DaskRunner
from microman import task


runner = DaskRunner('localhost:8281')

@task(runner=runner)
def do_stuff():
  pass
```

# Scheduling

# Lineage / Tracking


```python
from microman import task, persist, File

@task
def generate_report():
  ...
  return File()

```

## Metadata Storage

