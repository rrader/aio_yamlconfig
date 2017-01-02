import collections
import os

import yaml


class AppYAMLLoader(yaml.Loader):
    """
    Empty subclass of loader to add app-specific tags.
    """


class BaseYAMLConfig(collections.Mapping):
    def __init__(self, conf_file=None, trafaret_validator=None):
        super().__init__()
        self._raw = {}
        self._validated = {}

        self._trafaret = trafaret_validator
        self._YAMLLoader = AppYAMLLoader

        if conf_file:
            self.load(conf_file)

    def load(self, conf_file):
        with open(conf_file) as cfd:
            conf = yaml.load(cfd.read(), Loader=self._YAMLLoader)
        self._raw.update(conf)

    def validate(self):
        if self._trafaret:
            self._validated = self._trafaret.check(self._raw)
        else:
            self._validated = self._raw

    def register_tag(self, tag, callback):
        return yaml.add_constructor(tag, callback, Loader=self._YAMLLoader)

    def __len__(self):
        return len(self._validated)

    def __iter__(self):
        return iter(self._validated)

    def __getitem__(self, key):
        return self._validated[key]

    def __str__(self):
        if self._validated:
            return str(self._validated)
        else:
            return '<empty config>'


class AppYAMLConfig(BaseYAMLConfig):
    def __init__(self, conf_file=None, trafaret_validator=None, base_dir=None):
        super().__init__(conf_file, trafaret_validator)
        self._base_dir = base_dir
        self._setup_loader()

    def _tag_base_dir(self, loader, node):
        assert self._base_dir is not None, 'configuration contains !BaseDir options, but base_dir is not defined'
        return os.path.join(self._base_dir, loader.construct_scalar(node))

    def _tag_env_var(self, loader, node):
        env_var_name = loader.construct_scalar(node)
        return os.getenv(env_var_name)

    def _tag_first_of(self, loader, node):
        seq = loader.construct_sequence(node)
        for v in seq:
            if v is not None:
                return v

        raise yaml.YAMLError('At least one of values passed to !FirstOf tag must be not None')

    def _setup_loader(self):
        self.register_tag('!BaseDir', self._tag_base_dir)
        self.register_tag('!EnvVar', self._tag_env_var)
        self.register_tag('!FirstOf', self._tag_first_of)
