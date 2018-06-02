from setuptools import setup, find_packages

setup (
  name='Currency',
  version='1.0',
  packages=find_packages(),

  # Declare your packages' dependencies here, for eg:
  #       install_requires=['foo>=3'],

  # Fill in these to make your Egg ready for upload to
  # PyPI
  author='zhenya',
  author_email='telyukov@gmail.com',

  #summary = 'Just another Python package for the cheese shop',
  url='dummy.com',
  license='MIT',
  long_description="Game to guess country's currency",

  # could also include long_description, download_url, classifiers, etc.
)