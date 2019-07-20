from os import remove
from os.path import abspath, exists
from pathlib import Path
from unittest import TestCase
from thumbnailgen.util.common import get_root_dir
from thumbnailgen.util.config import Config
from thumbnailgen.models.singles_image import SinglesImage
from thumbnailgen.models.player import Player
from thumbnailgen.models.game import Game

GAME = Game('MELEE', 'SINGLES', 'Winners Finals')
PLAYER1 = Player('cookiE', 'Sheik', 'Neutral')
PLAYER2 = Player('Silver', 'Samus', 'Pink')
BACKGROUND_IMAGE = 'helloworld.jpg'
FOREGROUND_IMAGE = 'test.png'
LOGO_IMAGE = 'logo.png'

ROOT_DIR = get_root_dir()
DATA_DIR = str(Path(ROOT_DIR, 'test', 'data'))
CONFIG_FILE = str(Path(DATA_DIR, 'config.test.ini'))
TEST_OUTPUT_FILE = str(Path(DATA_DIR, 'test-singles-thumbnail.html'))


def read_file(file) -> str:
    with open(file, 'r') as f:
        return f.read()


class TestSinglesImage(TestCase):

    obj: SinglesImage = SinglesImage(
        height=1080,
        width=1920,
        background_image=BACKGROUND_IMAGE,
        foreground_image=FOREGROUND_IMAGE,
        logo_image=LOGO_IMAGE,
        filename=TEST_OUTPUT_FILE,
        game=GAME,
        player1=PLAYER1,
        player2=PLAYER2
    )
    config_obj = Config(file=CONFIG_FILE)
    expected_singles_file = abspath(Path(DATA_DIR, 'expected-thumbnail.singles.html'))
    unmarshalled_data = {
        'players': {
            'p1_tag': 'cookiE',
            'p2_tag': 'Silver',
            'p1_character': 'SHEIK',
            'p2_character': 'SAMUS',
            'p1_color': 'Neutral',
            'p2_color': 'Pink'
        },
        'game': {
            'round': 'Winners Finals',
            'name': 'MELEE',
            'type': 'SINGLES'
        },
        'image': {
            'background_image': 'helloworld.jpg',
            'foreground_image': 'test.png',
            'logo_image': 'logo.png'
        }
    }
    expected_marshalled_data = {
        'players': {
            'p1_tag': 'COOKIE',
            'p2_tag': 'SILVER',
            'p1_character': 'Sheik',
            'p2_character': 'Samus',
            'p1_color': 'neutral',
            'p2_color': 'pink'
        },
        'game': {
            'round': 'WINNERS FINALS',
            'name': 'Melee',
            'type': 'SINGLES'
        },
        'image': {
            'background_image': 'helloworld.jpg',
            'foreground_image': 'test.png',
            'logo_image': 'logo.png'
        }
    }

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        if exists(TEST_OUTPUT_FILE):
            remove(TEST_OUTPUT_FILE)

    def test_should_marshall_data_correctly_for_singles_image(self):
        expected = self.expected_marshalled_data
        actual = SinglesImage.marshall_data(self.unmarshalled_data)
        self.assertEqual(expected, actual)

    def test_pystache_template_is_written_correctly(self):
        expected = read_file(self.expected_singles_file)
        actual = self.obj.get_merged_template()
        self.assertEqual(expected, actual)

    def test_write_file_to_objects_filepath(self):
        expected = read_file(self.expected_singles_file)
        self.obj.write_file()

        self.assertTrue(exists(TEST_OUTPUT_FILE))
        with open(TEST_OUTPUT_FILE, 'r') as f:
            actual = f.read()
            self.assertEqual(expected, actual)

    def test_pystache_template_is_written_correctly_from_config(self):
        expected = read_file(self.expected_singles_file)
        actual = SinglesImage.get_merged_template_from_config(self.config_obj)
        self.assertEqual(expected, actual)

    def test_write_file_to_static_filepath(self):
        expected = read_file(self.expected_singles_file)
        SinglesImage.write_file_with_config(filepath=TEST_OUTPUT_FILE, config=self.config_obj)

        self.assertTrue(exists(TEST_OUTPUT_FILE))
        with open(TEST_OUTPUT_FILE, 'r') as f:
            actual = f.read()
            self.assertEqual(expected, actual)
