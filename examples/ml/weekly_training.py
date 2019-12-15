from microman import task


@task(schedule='weekly', start='12-13-2019', end=None)
def train():
  """
  Train a logistic regression model on
  """
  data = download_data('')
  data = preprocess(data)

  model = fit(data)



@task(cache=True, retries=3)
def download_data(uri: str):
  pass


@train.subtask()
def preprocess(data):
  return data


@train.subtask()
def fit(data):
  return ''


@task()
def save_model():
  pass


@train.then()
def evaluate():
  pass




train2 = (
    download_data
    > preprocess
    > fit
    > save_model
)

train2.schedule('weekly', start='last year', end='next year')