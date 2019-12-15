from microman import task

class Docker:
  def __init__(self, *args, **kwargs):
    pass

@task(runner=Docker('pytorch/pytorch:latest'))
def train_model():
  pass


