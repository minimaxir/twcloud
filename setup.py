from setuptools import setup, find_packages

long_description = '''
Generate a word cloud of [Twitter](https://twitter.com/) tweets with a single command.

twcloud is a Python package that leverages the [twint](https://github.com/twintproject/twint) package to gather Tweets from any public account without requiring authentication, and the [stylecloud](https://github.com/minimaxir/stylecloud) package which adds many useful features to create truly unique word clouds!

* Retrieve tweets from a user, or a Twitter search.
* Gather any number of Tweets from the specified query for building the word cloud (even beyond the typical 3,200 limit)
* Command Line Interface!

Additionally, from the base `stylecloud` package:

* Icon shapes (of any size!) for word clouds
* Support for advanced color palettes (via [palettable](https://jiffyclub.github.io/palettable/))
* Manual color selection for text and backgrounds,
* Directional gradients w/ the aforementioned palettes.
'''


setup(
    name='twcloud',
    packages=['twcloud'],  # this must be the same as the name above
    version='0.1',
    description="Python package + CLI to generate word clouds " \
    "of Twitter tweets.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Max Woolf',
    author_email='max@minimaxir.com',
    url='https://github.com/minimaxir/twcloud',
    keywords=['wordcloud', 'data visualization', 'text cool stuff'],
    classifiers=[],
    license='MIT',
    entry_points={
        'console_scripts': ['twcloud=twcloud.twcloud:twcloud_cli'],
    },
    python_requires='>=3.6',
    install_requires=['twint', 'stylecloud>=0.3']
)
