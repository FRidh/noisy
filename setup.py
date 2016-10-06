from setuptools import setup

CLASSIFIERS = [
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering',
    ]

setup(
    name='noisy',
    version='0.1',
    description='Noise of different colors',
    author='Frederik Rietdijk',
    author_email='fridh@fridh.nl',
    py_modules=['noisy'],
    install_requires=[
        'numpy',
        ],
    classifiers=CLASSIFIERS
    )
