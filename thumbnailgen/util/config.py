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
