# -*- coding: utf-8 -*-
import os

import configparser


class Config(object):
    def __init__(self, config_file='config.ini'):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            raise FileNotFoundError("No such file: {}".format(config_file))
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8')

global_config = Config()._config
order_config = Config(config_file='order_config.ini')._config
