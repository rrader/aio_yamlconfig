import os

import trafaret as t


class ExistingDirectory(t.String):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def check_value(self, value):
        if not os.path.isdir(value):
            raise t.DataError(error='{} is not directory'.format(value))
