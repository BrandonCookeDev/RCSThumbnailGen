from pathlib import Path
from thumbnailgen.util.common import get_json_dir
from thumbnailgen.util.exceptions import NotImplementedException


class Image(object):

	def __init__(self, height=720, width=1080):
		self.height = height
		self.width = width
		self.json_file = str(Path(get_json_dir(), 'image.json'))

	def write_data(self):
		raise NotImplementedException()

	def draw(self):
		raise NotImplementedException()