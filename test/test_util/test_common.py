from os import getenv
from os.path import abspath, dirname
from pathlib import Path
from unittest import TestCase
from thumbnailgen.util.common import get_root_dir, \
    get_test_dir, get_css_dir, get_web_dir, get_json_dir, \
    get_resources_dir, capitalize_word

ROOT_DIR = dirname(abspath(Path(__file__, '..', '..')))

class TestCommon(TestCase):

    expected_root_dir = ROOT_DIR
    expected_test_dir = str(Path(ROOT_DIR, 'test'))
    expected_resources_dir = str(Path(ROOT_DIR, 'resources'))
    expected_web_dir = str(Path(ROOT_DIR, 'resources', 'web'))
    expected_css_dir = str(Path(ROOT_DIR, 'resources', 'web', 'styles'))
    expected_json_dir = str(Path(ROOT_DIR, 'resources', 'web', 'json'))

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_root_dir(self):
        actual = get_root_dir()
        self.assertEqual(self.expected_root_dir, actual)

    def test_get_resources_dir(self):
        actual = get_resources_dir()
        self.assertEqual(self.expected_resources_dir, actual)

    def test_get_test_dir(self):
        actual = get_test_dir()
        self.assertEqual(self.expected_test_dir, actual)

    def test_get_web_dir(self):
        actual = get_web_dir()
        self.assertEqual(self.expected_web_dir, actual)

    def test_get_css_dir(self):
        actual = get_css_dir()
        self.assertEqual(self.expected_css_dir, actual)

    def test_get_json_dir(self):
        actual = get_json_dir()
        self.assertEqual(self.expected_json_dir, actual)

    def test_captializes_a_lowercase_word(self):
        data = 'hello'
        expected = 'Hello'
        actual = capitalize_word(data)
        self.assertEqual(expected, actual)

    def test_captializes_an_uppercase_word(self):
        data = 'HELLO'
        expected = 'Hello'
        actual = capitalize_word(data)
        self.assertEqual(expected, actual)
