from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = """sweetmorse
----------

Morse code tools from read to write, analog to digital.

.. image:: https://www.travis-ci.org/Jdsleppy/sweetmorse.svg?branch=master
    :target: https://www.travis-ci.org/Jdsleppy/sweetmorse

Compatibility
-------------

Targets Python3, tested against against Python 3.3-3.6.

More info
---------

See a crash course at https://github.com/Jdsleppy/sweetmorse
"""

setup(
    name='sweetmorse',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='Morse code tools from read to write, analog to digital',
    long_description=long_description,

    url='https://github.com/Jdsleppy/sweetmorse',

    author='Joel Sleppy',
    author_email='jdsleppy@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Communications :: Ham Radio',
        'Topic :: Multimedia :: Sound/Audio',

        # (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='morse signal electronics',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['tests']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],

    python_requires='~=3.0',

    package_data={},

    data_files=[],

    entry_points={
        'console_scripts': [
            'sweetmorse = sweetmorse.main:main',
        ],
    },
)
