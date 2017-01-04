.. image:: https://img.shields.io/pypi/v/aio_yamlconfig.svg
   :target: https://pypi.org/project/aio_yamlconfig

.. image:: https://img.shields.io/travis/rrader/aio_yamlconfig/master.svg
   :target: http://travis-ci.org/rrader/aio_yamlconfig

.. image:: https://img.shields.io/pypi/pyversions/aio_yamlconfig.svg

.. image:: https://img.shields.io/pypi/dm/aio_yamlconfig.svg


aio_yamlconfig
========

Quick Start
------------------

Install from PYPI:

.. code:: shell

    pip install aio_yamlconfig

OR (less popular) via setup.py:

.. code:: shell

    python -m setup install

YAML configuration parser with validation using `Trafaret <http://trafaret.readthedocs.org/en/latest/>`_.

In the easiest setup without config validation, configure your ``aiohttp`` application with:

.. code:: python
   :number-lines:

    CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.yaml")
    loop.run_until_complete(aio_yamlconfig.setup(app,
                                                 config_files=[CONFIG_FILE],
                                                 base_dir=os.path.dirname(__file__)))

Assume you have ``config.yaml``:

.. code:: yaml
   :number-lines:

    DEBUG: True
    TEMPLATES_DIR: !BaseDir path/to/templates

Then you can access your config as:

.. code:: python
   :number-lines:

    if app.config['DEBUG']:
        print('some debug information')

Notice the ``!BaseDir`` tag. ``aio_yamlconfig`` can do some config transformations for you, in this case it will prepend
the base directory (passed as ``base_dir`` to ``setup()``) to your path. The variable ``app.config['TEMPLATES_DIR']`` will contain
the full path to directory with your templates.

Validation
--------------------

To validate your config we use the great library Trafaret. You can read more about it `in the docs <http://trafaret.readthedocs.org/en/latest/>`_.
Here I'll give you a simple example of its usage.

Let's write the validator for ``config.yaml`` above. We'd like to ensure that ``DEBUG`` value is boolean, and that
directory of the path ``TEMPLATES_DIR`` really exists:

.. code:: python
   :number-lines:

    import trafaret as t
    from aio_yamlconfig.trafarets import ExistingDirectory

    CONFIG_TRAFARET = t.Dict({
        t.Key('TEMPLATES_DIR'): ExistingDirectory,
        t.Key('DEBUG'): t.Bool
    })


To enable such validation pass the ``trafaret_validator`` to ``setup()`` function:

.. code:: python
   :number-lines:

    loop.run_until_complete(aio_yamlconfig.setup(app,
                                                 config_files=[CONFIG_FILE],
                                                 trafaret_validator=CONFIG_TRAFARET,
                                                 base_dir=os.path.dirname(__file__)))
