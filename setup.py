from setuptools import setup, find_packages

long_description = '''

'''


setup(
    name='twcloud',
    packages=['twcloud'],  # this must be the same as the name above
    version='0.1',
    description="Python package + CLI to generate wordclouds " \
    "of Twitter tweets",
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
