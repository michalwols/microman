from microman import task, Params
import random


@task
def estimate_story_points(story):
  return random.randint(1, 12)

def plan_stories():
  return [
    'schedule meetings',
    'have standup',
  ]

@task(schedule='daily', start='2019')
def have_meeting():
  stories = plan_stories()
  for story in stories:
    estimate_story_points(story)

have_meeting()

for run in estimate_story_points.runs:
  print(run.task.name, ':', *run.inputs, '>', run.outputs)