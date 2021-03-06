from pathlib import Path

from thumbnailgen.models.game import Game
from thumbnailgen.models.image import Image
from thumbnailgen.models.player import Player
from thumbnailgen.util.common import get_web_dir
from thumbnailgen.util.exceptions import NotImplementedException

class DoublesImage(Image):

    def __init__(self, height, width,
                 background_image=None,
                 foreground_image=None,
                 logo_image=None,
                 game: Game = Game('MELEE', 'DOUBLES'),
                 filename='doubles-thumbnail.html',
                 player1: Player = Player(),
                 player2: Player = Player(),
                 player3: Player = Player(),
                 player4: Player = Player()):
        super().__init__(height, width,background_image, foreground_image, logo_image, game)
        self.html_file = str(Path(get_web_dir(), filename))
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4

    def get_merged_template(self):
        raise NotImplementedException()

    def write_file(self):
        raise NotImplementedException()

    @staticmethod
    def get_template():
        raise NotImplementedException()

    @staticmethod
    def get_merged_template_from_config():
        raise NotImplementedException()

    @staticmethod
    def marshall_data():
        raise NotImplementedException()

    @staticmethod
    def write_file_with_config():
        raise NotImplementedException()