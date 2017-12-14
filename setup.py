from os import path
from setuptools import setup

with open(path.join(path.abspath(path.dirname(__file__)), 'README'), encoding='utf-8') as f:
    long_description = f.read()
with open(path.join(path.abspath(path.dirname(__file__)), 'VERSION'), encoding='utf-8') as f:
    version = f.read()

setup(name="tf_logger",
      description="A print and debugging utility that makes your error printouts look nice",
      long_description=long_description,
      version=version,
      url="https://github.com/episodeyang/tf_logger",
      author="Ge Yang",
      author_email="yangge1987@gmail.com",
      license=None,
      keywords=["tf_logger", "logging", "debug", "debugging", "timer", "timeit", "decorator",
                "stopwatch", "tic", "toc"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "Programming Language :: Python :: 3"
      ],
      packages=["tf_logger"],
      install_requires=["termcolor", "pprint"]
      )
