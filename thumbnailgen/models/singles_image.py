import json
from pathlib import Path

from thumbnailgen.models.game import Game
from thumbnailgen.models.image import Image
from thumbnailgen.models.player import Player
from thumbnailgen.util.common import get_web_dir


class SinglesImage(Image):

    def __init__(self, height=720, width=1080,
                 background_image=None,
                 foreground_image=None,
                 filename='singles-thumbnail.html',
                 game: Game = Game('MELEE', 'SINGLES'),
                 player1: Player = Player(),
                 player2: Player = Player()):
        super().__init__(height, width, background_image, foreground_image, game)
        self.html_file = str(Path(get_web_dir(), filename))
        self.player1 = player1
        self.player2 = player2

    def write_data(self):
        pass

    def draw(self):
        pass
