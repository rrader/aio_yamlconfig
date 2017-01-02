from aio_yamlconfig.config import AppYAMLConfig


async def setup_empty(app, **kwargs):
    """
    Setup empty config for manual loading configs.
    After setup user need to do:

     app.config.load("config1.yaml")
     app.config.load("config2.yaml")
     app.config.validate()
    """
    app['config'] = AppYAMLConfig(**kwargs)
    # setup attribute to access config via
    #
    # app.config['section']['name']
    app.config = app['config']


async def setup(app, config_files, base_dir, **kwargs):
    await setup_empty(app, base_dir=base_dir, **kwargs)

    for f in config_files:
        app.config.load(f)
    app.config.validate()
