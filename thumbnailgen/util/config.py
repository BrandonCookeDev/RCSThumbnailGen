import json
from configparser import ConfigParser
from pathlib import Path
from os.path import exists, isabs, abspath

CONFIG_DIR = abspath(Path(__file__, '..', '..', 'config'))
CONFIG_FILE = str(Path(CONFIG_DIR, 'config.ini'))


class Config(object):
    def __init__(self, file=CONFIG_FILE):
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

    def get_game_name(self):
        return str(self.config.get('GAME', 'game_name'))

    def get_game_type(self):
        return str(self.config.get('GAME', 'game_type'))

    def get_config_object(self) -> dict:
        return {
            'image': {
                'height': self.get_image_height(),
                'width': self.get_image_width(),
                'backgroundImage': self.get_image_background(),
                'foregroundImage': self.get_image_foreground()
            },
            'players': {
                'p1Tag': self.get_player_1_tag(),
                'p2Tag': self.get_player_2_tag(),
                'p3Tag': self.get_player_3_tag(),
                'p4Tag': self.get_player_4_tag(),
                'p1Character': self.get_player_1_character(),
                'p2Character': self.get_player_2_character(),
                'p3Character': self.get_player_3_character(),
                'p4Character': self.get_player_4_character()
            },
            'game': {
                'name': self.get_game_name(),
                'type': self.get_game_type()
            }
        }

    def get_config_json(self) -> str:
        return json.dumps(self.get_config_object)