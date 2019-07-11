import json
from unittest import TestCase
from pathlib import Path
from os.path import exists, abspath

from thumbnailgen.util.config import Config
from thumbnailgen.util.common import get_root_dir

ROOT_DIR = get_root_dir()


class TestConfig(TestCase):
    DATA_DIR = str(Path(ROOT_DIR, 'test', 'data'))
    CONFIG_FILE = str(Path(DATA_DIR, 'config.test.ini'))
    config_obj = None
    config_py_obj = {
        'image': {
            'height': 1080,
            'width': 1920,
            'background_image': 'helloworld.jpg',
            'foreground_image': 'test.png',
            'logo_image': 'logo.png'
        },
        'players': {
            'p1_tag': 'cookiE',
            'p2_tag': 'Silver',
            'p3_tag': 'SDeems',
            'p4_tag': 'Slips',
            'p1_character': 'Sheik',
            'p2_character': 'Samus',
            'p3_character': 'Fox',
            'p4_character': 'Luigi',
            'p1_color': 'Blue',
            'p2_color': 'Neutral',
            'p3_color': 'Green',
            'p4_color': 'Red'
        },
        'game': {
            'name': 'MELEE',
            'type': 'SINGLES',
            'round': 'Winners Finals'
        }
    }

    def setUp(self):
        self.config_obj = Config(self.CONFIG_FILE)

    def tearDown(self):
        self.config_obj = None

    def test_should_get_height_from_config(self):
        self.assertEqual(1080, self.config_obj.get_image_height())

    def test_should_get_width_from_config(self):
        self.assertEqual(1920, self.config_obj.get_image_width())

    def test_should_get_background_image_from_config(self):
        self.assertEqual('helloworld.jpg', self.config_obj.get_image_background())

    def test_should_get_foreground_image_from_config(self):
        self.assertEqual('test.png', self.config_obj.get_image_foreground())

    def test_should_get_player_1_tag_from_config(self):
        self.assertEqual('cookiE', self.config_obj.get_player_1_tag())

    def test_should_get_player_2_tag_from_config(self):
        self.assertEqual('Silver', self.config_obj.get_player_2_tag())

    def test_should_get_player_3_tag_from_config(self):
        self.assertEqual('SDeems', self.config_obj.get_player_3_tag())

    def test_should_get_player_4_tag_from_config(self):
        self.assertEqual('Slips', self.config_obj.get_player_4_tag())

    def test_should_get_player_1_character_from_config(self):
        self.assertEqual('Sheik', self.config_obj.get_player_1_character())

    def test_should_get_player_2_character_from_config(self):
        self.assertEqual('Samus', self.config_obj.get_player_2_character())

    def test_should_get_player_3_character_from_config(self):
        self.assertEqual('Fox', self.config_obj.get_player_3_character())

    def test_should_get_player_4_character_from_config(self):
        self.assertEqual('Luigi', self.config_obj.get_player_4_character())

    def test_should_get_player_1_color_from_config(self):
        self.assertEqual('Blue', self.config_obj.get_player_1_color())

    def test_should_get_player_2_color_from_config(self):
        self.assertEqual('Neutral', self.config_obj.get_player_2_color())

    def test_should_get_player_3_color_from_config(self):
        self.assertEqual('Green', self.config_obj.get_player_3_color())

    def test_should_get_player_4_color_from_config(self):
        self.assertEqual('Red', self.config_obj.get_player_4_color())

    def test_should_get_game_name_from_config(self):
        self.assertEqual('MELEE', self.config_obj.get_game_name())

    def test_should_get_game_type_from_config(self):
        self.assertEqual('SINGLES', self.config_obj.get_game_type())

    def test_should_get_game_round_from_config(self):
        self.assertEqual('Winners Finals', self.config_obj.get_game_round())

    def test_should_get_the_correct_config_object_back(self):
        expected = self.config_py_obj
        actual = self.config_obj.get_config_object()
        self.assertEqual(expected, actual)

    def test_should_get_the_correct_config_json_back(self):
        expected = json.dumps(self.config_py_obj)
        actual = self.config_obj.get_config_json()
        self.assertEqual(expected, actual)
