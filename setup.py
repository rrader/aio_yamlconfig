import os

from setuptools import setup, find_packages


__version__ = '0.2.0'


classifiers = [
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Environment :: Web Environment',
    'Development Status :: 4 - Beta',
]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='aio_yamlconfig',
      version=__version__,
      description='YAML configuration parser with validation.',
      long_description=read('README.rst'),
      classifiers=classifiers,
      platforms=['POSIX'],
      author='Roman Rader',
      author_email='antigluk@gmail.com',
      url='https://github.com/rrader/aio_yamlconfig',
      license='BSD',
      packages=find_packages(),
      install_requires=['trafaret', 'PyYAML'],
      include_package_data=True)
