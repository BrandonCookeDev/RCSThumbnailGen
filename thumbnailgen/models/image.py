from pathlib import Path
from thumbnailgen.models.game import Game
from thumbnailgen.util.common import get_json_dir
from thumbnailgen.util.exceptions import NotImplementedException


class Image(object):

	def __init__(self, height=720, width=1080,
				 background_image=None,
				 foreground_image=None,
				 game: Game = Game()):
		self.height = height
		self.width = width
		self.background_image = background_image
		self.foreground_image = foreground_image
		self.game = game
		self.json_file = str(Path(get_json_dir(), 'image.json'))

	def write_data(self):
		raise NotImplementedException()

	def draw(self):
		raise NotImplementedException()