import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__),
                       'README')) as f:
    readme = f.read().strip()


setup(
    name='python-geoip-yplan',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    maintainer='Thomas Grainger',
    maintainer_email='python-geoip-yplan@graingert.co.uk',
    version='1.2',
    url='https://github.com/yplan/python-geoip',
    long_description=readme,
    description='Provides GeoIP functionality for Python.',
    py_modules=['geoip'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: BSD License',
    ],
)
