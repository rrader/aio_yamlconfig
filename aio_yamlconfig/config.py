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
            return "<empty config>"


class AppYAMLConfig(BaseYAMLConfig):
    def __init__(self, conf_file=None, trafaret_validator=None, base_dir=None):
        super().__init__(conf_file, trafaret_validator)
        self._base_dir = base_dir
        self._setup_loader()

    def _tag_base_dir(self, loader, node):
        assert self._base_dir is not None, "configuration contains !BaseDir options, but base_dir is not defined"
        return os.path.join(self._base_dir, loader.construct_scalar(node))

    def _setup_loader(self):
        yaml.add_constructor("!BaseDir", self._tag_base_dir, Loader=self._YAMLLoader)
