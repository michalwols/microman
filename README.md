
# microman - Micromanager

![micromanaging](docs/images/comic.jpg)



## What is micromanaging? 

> Micromanaging is a management style where you have excessive control over every detail and aspect of the project without regard to the impact on others or yourself.
>
> 1. Have a hard time asking for help
> 1. Check in frequently to see if the work is being done/done your way
> 1. Monitor every detail, even the smallest ones
> 1. Believe that no one can produce what you can
> 1. Don’t take advice or suggestions from others
> 1. Make all the decisions involved in the project
> 1. Believe others are likely to waste time or resources
>
> [- source](https://www.outsourceeasier.com/micromanager/)

microman is your boss's favorite tool, it:

1. Tracks task execution
2. Schedules all of your work
3. Keeps track of artifacts
4. Helps you outsource common tasks
5. Dynamically executes tasks
6. Automates you out of your job

# Getting started

```commandline
pip install microman
```



```python
from microman import task


@task
def train_model():
  pass
```


```commandline
microman run
```


```commandline
microman tasks status=running
```

```commandline
microman run train_model
```


```commandline
microman schedule train_model tomorrow
```



## Delegating Tasks

```commandline
from microman.tasks.slack import send_message
from microman.tasks.gcp import download, upload
from microman.tasks.spacy import tag


@task
def train(log: Prop=None, time_created: Prop=None):
  pass

```