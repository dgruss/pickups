import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "hangups",
    version = "prototype",
    author = "Michael Tom-Wing",
    author_email = "mtomwing",
    description = ("IRC gateway for hangups"),
    license = "MIT",
    keywords = "irc gateway google hangouts",
    url = "https://github.com/mtomwing/pickups",
    packages=['pickups'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
