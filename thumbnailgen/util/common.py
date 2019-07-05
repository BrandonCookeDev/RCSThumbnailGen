from pathlib import Path
from os.path import exists, abspath, isabs

RESOURCES_DIR = abspath(Path(__file__, '..', '..', 'resources'))
WEB_DIR = str(Path(RESOURCES_DIR, 'web'))
CSS_DIR = str(Path(WEB_DIR, 'styles'))
JSON_DIR = str(Path(WEB_DIR, 'json'))


def get_web_dir():
    return WEB_DIR


def get_css_dir():
    return CSS_DIR


def get_json_dir():
    return JSON_DIR


def get_resources_dir():
    return RESOURCES_DIR
