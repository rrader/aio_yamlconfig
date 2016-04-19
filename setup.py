import os

from setuptools import setup, find_packages


classifiers = [
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Environment :: Web Environment',
    'Development Status :: 4 - Beta',
]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='aio_yamlconfig',
      version='0.1.0',
      description='YAML configuration parser with validation.',
      long_description=read('README.rst'),
      classifiers=classifiers,
      platforms=['POSIX'],
      author='Roman Rader',
      author_email='antigluk@gmail.com',
      url='https://github.com/rrader/aio_yamlconfig',
      license='BSD',
      packages=find_packages(),
      install_requires=['trafaret', 'yaml'],
      include_package_data = True)
