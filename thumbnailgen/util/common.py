from pathlib import Path
from os.path import exists, abspath, isabs, dirname

ROOT_DIR = dirname(abspath(Path(__file__, '..', '..')))
RESOURCES_DIR = str(Path(ROOT_DIR, 'resources'))
TEST_DIR = str(Path(ROOT_DIR, 'test'))
WEB_DIR = str(Path(RESOURCES_DIR, 'web'))
CSS_DIR = str(Path(WEB_DIR, 'styles'))
JSON_DIR = str(Path(WEB_DIR, 'json'))


def get_root_dir():
    return ROOT_DIR


def get_test_dir():
    return TEST_DIR


def get_web_dir():
    return WEB_DIR


def get_css_dir():
    return CSS_DIR


def get_json_dir():
    return JSON_DIR


def get_resources_dir():
    return RESOURCES_DIR


def capitalize_word(word: str) -> str:
    return word[0].upper() + word[1:].lower()
