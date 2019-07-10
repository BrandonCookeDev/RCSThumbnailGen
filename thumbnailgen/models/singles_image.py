import json
import pystache
from os.path import exists, abspath
from pathlib import Path

from thumbnailgen.models.game import Game
from thumbnailgen.models.image import Image
from thumbnailgen.models.player import Player
from thumbnailgen.util.config import Config
from thumbnailgen.util.common import get_web_dir
from thumbnailgen.util.io import get_file_content

TEMPLATE_DIR = abspath(Path('..', '..', 'resources', 'web', 'templates'))
TEMPLATE_FILE = str(Path(TEMPLATE_DIR, 'singles-thumbnail-template.html'))


class SinglesImage(Image):

    def __init__(self, height=1080, width=1920,
                 background_image=None,
                 foreground_image=None,
                 logo_image=None,
                 filename='singles-thumbnail.html',
                 game: Game = Game('MELEE', 'SINGLES'),
                 player1: Player = Player(),
                 player2: Player = Player()):
        super().__init__(height, width, background_image, foreground_image, logo_image, game)
        self.html_file = str(Path(get_web_dir(), filename))
        self.player1 = player1
        self.player2 = player2

    def write_data(self, config=Config()):
        template = get_file_content(TEMPLATE_FILE)
        config_data = config.get_config_object()
        merged = pystache.render(template, config_data)
        return merged

    def draw(self):
        pass
