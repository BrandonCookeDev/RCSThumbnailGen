from os.path import abspath
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


def read_file(file) -> str:
    with open(file, 'r') as f:
        return f.read()


class TestSinglesImage(TestCase):

    obj: SinglesImage = SinglesImage(
        height=1080,
        width=720,
        background_image=BACKGROUND_IMAGE,
        foreground_image=FOREGROUND_IMAGE,
        logo_image=LOGO_IMAGE,
        filename='test-thumbnail.html',
        game=GAME,
        player1=PLAYER1,
        player2=PLAYER2
    )
    config_obj = Config(file=CONFIG_FILE)
    expected_singles_file = abspath(Path('..', 'data', 'expected-thumbnail.singles.html'))

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_pystache_template_is_written_correctly(self):
        expected = read_file(self.expected_singles_file)
        actual = self.obj.write_data(self.config_obj)
        self.assertEqual(expected, actual)
