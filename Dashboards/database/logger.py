#!/usr/bin/env python


import os
import logging.config
import yaml

# Pattern from: https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/


def setup_logging(
        default_path='logging.yaml',
        default_level=logging.INFO,
        env_key='LOG_CFG'):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as file_h:
            config = yaml.safe_load(file_h.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)