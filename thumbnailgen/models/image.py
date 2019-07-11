from pathlib import Path
from thumbnailgen.models.game import Game
from thumbnailgen.util.common import get_json_dir
from thumbnailgen.util.exceptions import NotImplementedException


class Image(object):

    def __init__(self, height=1080, width=1920,
                 background_image=None,
                 foreground_image=None,
                 logo_image=None,
                 game: Game = Game()):
        self.height = height
        self.width = width
        self.background_image = background_image
        self.foreground_image = foreground_image
        self.logo_image = logo_image
        self.game = game
        self.json_file = str(Path(get_json_dir(), 'image.json'))

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