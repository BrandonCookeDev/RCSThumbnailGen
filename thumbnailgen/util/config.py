import json
from configparser import ConfigParser
from pathlib import Path
from os.path import exists, isabs, abspath

CONFIG_DIR = abspath(Path(__file__, '..', '..', '..', 'config'))
CONFIG_FILE = str(Path(CONFIG_DIR, 'config.ini'))


class Config(object):
    def __init__(self, file=CONFIG_FILE):
        if not exists(file):
            raise Exception('config file does not exist: {}'.format(file))
        self.file = file
        self.config = ConfigParser()
        self.config.read(self.file)

    def get_image_height(self) -> int:
        return int(self.config.get('IMAGE', 'height'))

    def get_image_width(self) -> int:
        return int(self.config.get('IMAGE', 'width'))

    def get_image_background(self):
        return str(self.config.get('IMAGE', 'background_image'))

    def get_image_foreground(self):
        return str(self.config.get('IMAGE', 'foreground_image'))

    def get_image_logo(self):
        return str(self.config.get('IMAGE', 'logo_image'))

    def get_player_1_tag(self):
        return str(self.config.get('PLAYERS', 'p1_tag'))

    def get_player_2_tag(self):
        return str(self.config.get('PLAYERS', 'p2_tag'))

    def get_player_3_tag(self):
        return str(self.config.get('PLAYERS', 'p3_tag'))

    def get_player_4_tag(self):
        return str(self.config.get('PLAYERS', 'p4_tag'))

    def get_player_1_character(self):
        return str(self.config.get('PLAYERS', 'p1_character'))

    def get_player_2_character(self):
        return str(self.config.get('PLAYERS', 'p2_character'))

    def get_player_3_character(self):
        return str(self.config.get('PLAYERS', 'p3_character'))

    def get_player_4_character(self):
        return str(self.config.get('PLAYERS', 'p4_character'))

    def get_player_1_color(self):
        return str(self.config.get('PLAYERS', 'p1_color'))

    def get_player_2_color(self):
        return str(self.config.get('PLAYERS', 'p2_color'))

    def get_player_3_color(self):
        return str(self.config.get('PLAYERS', 'p3_color'))

    def get_player_4_color(self):
        return str(self.config.get('PLAYERS', 'p4_color'))

    def get_game_name(self):
        return str(self.config.get('GAME', 'game_name'))

    def get_game_type(self):
        return str(self.config.get('GAME', 'game_type'))

    def get_game_round(self):
        return str(self.config.get('GAME', 'game_round'))

    def get_config_object(self) -> dict:
        return {
            'image': {
                'height': self.get_image_height(),
                'width': self.get_image_width(),
                'background_image': self.get_image_background(),
                'foreground_image': self.get_image_foreground(),
                'logo_image': self.get_image_logo()
            },
            'players': {
                'p1_tag': self.get_player_1_tag(),
                'p2_tag': self.get_player_2_tag(),
                'p3_tag': self.get_player_3_tag(),
                'p4_tag': self.get_player_4_tag(),
                'p1_character': self.get_player_1_character(),
                'p2_character': self.get_player_2_character(),
                'p3_character': self.get_player_3_character(),
                'p4_character': self.get_player_4_character(),
                'p1_color': self.get_player_1_color(),
                'p2_color': self.get_player_2_color(),
                'p3_color': self.get_player_3_color(),
                'p4_color': self.get_player_4_color()
            },
            'game': {
                'name': self.get_game_name(),
                'type': self.get_game_type(),
                'round': self.get_game_round()
            }
        }

    def get_config_json(self) -> str:
        return json.dumps(self.get_config_object())