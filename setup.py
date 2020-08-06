from setuptools import setup

setup(
    name='PyFormative',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
        'yattag'
    ],
    entry_points='''
        [console_scripts]
        PyFormative=main:initial
    ''',
)