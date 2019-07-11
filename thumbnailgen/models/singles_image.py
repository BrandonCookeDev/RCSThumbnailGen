import json
import pystache
from os.path import exists, abspath
from pathlib import Path
from copy import deepcopy

from thumbnailgen.models.game import Game
from thumbnailgen.models.image import Image
from thumbnailgen.models.player import Player
from thumbnailgen.util.config import Config
from thumbnailgen.util.io import get_file_content
from thumbnailgen.util.common import get_root_dir, \
    get_web_dir, capitalize_word

ROOT_DIR = get_root_dir()
OUTPUT_DIR = str(Path(ROOT_DIR, 'resources', 'web', 'output'))
TEMPLATE_DIR = str(Path(ROOT_DIR, 'resources', 'web', 'templates'))
TEMPLATE_FILE = str(Path(TEMPLATE_DIR, 'singles-thumbnail-template.html'))
DEFAULT_OUTPUT_FILE = str(Path(OUTPUT_DIR, 'singles-thumbnail.html'))


class SinglesImage(Image):

    def __init__(self, height=1080, width=1920,
                 background_image=None,
                 foreground_image=None,
                 logo_image=None,
                 filename=DEFAULT_OUTPUT_FILE,
                 game: Game = Game('MELEE', 'SINGLES'),
                 player1: Player = Player(),
                 player2: Player = Player()):
        super().__init__(height, width, background_image, foreground_image, logo_image, game)
        self.html_file = str(Path(get_web_dir(), filename))
        self.player1 = player1
        self.player2 = player2

    def get_merged_template(self):
        template = SinglesImage.get_template()
        merge_data = {
            'players': {
                'p1_tag': str(self.player1.tag).upper(),
                'p2_tag': str(self.player2.tag).upper(),
                'p1_character': str(self.player1.character).lower(),
                'p2_character': str(self.player2.character).lower(),
                'p1_color': capitalize_word(self.player1.color),
                'p2_color': capitalize_word(self.player2.color),
            },
            'image': {
                'background_image': self.background_image,
                'foreground_image': self.foreground_image,
                'logo_image': self.logo_image,
            },
            'game': {
                'round': str(self.game.round).upper()
            }
        }
        merge_data = SinglesImage.marshall_data(merge_data)
        merged = pystache.render(template, merge_data)
        return merged

    def write_file(self):
        merged_template = self.get_merged_template()
        with open(self.html_file, 'w') as f:
            f.write(merged_template)
            
        print('wrote thumbnail file to {}'.format(self.html_file))

    @staticmethod
    def get_template():
        return get_file_content(TEMPLATE_FILE)

    @staticmethod
    def get_merged_template_from_config(config=Config()):
        template = SinglesImage.get_template()
        config_data = deepcopy(config.get_config_object())
        config_data = SinglesImage.marshall_data(config_data)
        merged = pystache.render(template, config_data)
        return merged

    @staticmethod
    def marshall_data(data: dict) -> dict:
        config_copy = deepcopy(data)
        config_copy['players']['p1_tag'] = config_copy['players']['p1_tag'].upper()
        config_copy['players']['p2_tag'] = config_copy['players']['p2_tag'].upper()
        config_copy['players']['p1_character'] = config_copy['players']['p1_character'].lower()
        config_copy['players']['p2_character'] = config_copy['players']['p2_character'].lower()
        config_copy['players']['p1_color'] = capitalize_word(config_copy['players']['p1_color'])
        config_copy['players']['p2_color'] = capitalize_word(config_copy['players']['p2_color'])
        config_copy['game']['round'] = config_copy['game']['round'].upper()
        return config_copy

    @staticmethod
    def write_file_with_config(filepath, config=Config()):
        merged_template = SinglesImage.get_merged_template_from_config(config)
        with open(filepath, 'w') as f:
            f.write(merged_template)