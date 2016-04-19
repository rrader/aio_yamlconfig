aio_yamlconfig
========

Quick Start
------------------

YAML configuration parser with validation using Trafaret ( http://trafaret.readthedocs.org/en/latest/ ).

In the easiest setup without config validation, configure you aiohttp application with::

    CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.yaml")
    loop.run_until_complete(aio_yamlconfig.setup(app,
                                                 config_files=[CONFIG_FILE],
                                                 base_dir=os.path.dirname(__file__)))

Assume you have `config.yaml`::

    DEBUG: True
    TEMPLATES_DIR: !BaseDir path/to/templates

Then you can access your config as::

    if app.config['DEBUG']:
        print('some debug information')

Notice the `!BaseDir` tag. aio_yamlconfig can do some config transformations for you, in this case it will prepend
the base directory (passed as `base_dir` in setup) to your path. The variable app.config['TEMPLATES_DIR'] will contain
the full path to directory with your templates.

Validation
--------------------

To validate your config we use the great library Trafaret. You can read more about it in the docs,
 http://trafaret.readthedocs.org/en/latest/ . Here I'll give simple example of the usage.

Let's write the validator for `config.yaml` above. We'd like to assure that `DEBUG` value is boolean, and that
directory by the path `TEMPLATES_DIR` really exists::

    import trafaret as t
    from aio_yamlconfig.trafarets import ExistingDirectory

    CONFIG_TRAFARET = t.Dict({
        t.Key('TEMPLATES_DIR'): ExistingDirectory,
        t.Key('DEBUG'): t.Bool
    })


To enable validation pass the `trafaret_validator` to the setup function::

    loop.run_until_complete(aio_yamlconfig.setup(app,
                                                 config_files=[CONFIG_FILE],
                                                 trafaret_validator=CONFIG_TRAFARET,
                                                 base_dir=os.path.dirname(__file__)))
