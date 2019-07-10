from os import remove
from os.path import abspath, exists
from pathlib import Path
from unittest import TestCase
from thumbnailgen.util.config import Config
from thumbnailgen.models.singles_image import SinglesImage
from thumbnailgen.models.player import Player
from thumbnailgen.models.game import Game

GAME = Game('MELEE', 'SINGLES', 'Winners Finals')
PLAYER1 = Player('cookiE', 'Sheik', 'Blue')
PLAYER2 = Player('Silver', 'Samus', 'Neutral')
BACKGROUND_IMAGE = 'helloworld.jpg'
FOREGROUND_IMAGE = 'test.png'
LOGO_IMAGE = 'logo.png'

DATA_DIR = abspath(Path('..', 'data'))
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
    expected_singles_file = abspath(Path('..', 'data', 'expected-thumbnail.singles.html'))

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        if exists(TEST_OUTPUT_FILE):
            remove(TEST_OUTPUT_FILE)

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
