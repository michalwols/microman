from microman import task, background
from microman.tasks import bash




@task
def create_django_server():
  bash.command('django createsuperuser')







