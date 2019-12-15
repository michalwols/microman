from setuptools import setup, find_packages

# with open("README.md", "r") as fh:
#   long_description = fh.read()


long_description = f"""
# microman

Microman is a simple task execution manager and tracker. 
"""


setup(
  name='microman',
  version='0.0.1',
  description='micromanage all of your tasks',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/michalwols/microman',
  author='Michal Wolski',
  author_email='michalwols@gmail.com',
  license='MIT',
  packages=find_packages(),
  entry_points={
    'console_scripts': ['microman=microman.cli:main'],
  },
  extras_require={
    'cli': ['click>=6.7']
  },
  install_requires=[],
  python_requires='>=3.7',
  zip_safe=False
)