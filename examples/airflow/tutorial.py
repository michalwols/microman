# https://airflow.apache.org/docs/stable/tutorial.html

from microman import task, Param
from microman.tasks import bash, email

templated_command = bash.Command(
  template="""
   {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
  """
)


@task(
  retries=1,
  retry_policy='sleep',
  priority=18,
  start='10-10-2019',
  schedule='weekly',
  meta=dict(
    owner='microman',
    project='airflow-tutorial'
  )
)
def tutorial_example():
  date = bash.command('date')
  bash.command('sleep', retries=3)
  templated_command(my_param=Param('my_param'))


@tutorial_example.on.complete
def email():
  email.send()


tutorial_example.backfill()
