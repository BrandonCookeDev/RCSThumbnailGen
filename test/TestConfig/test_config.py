from unittest import TestCase
from pathlib import Path
from os.path import exists, abspath

from thumbnailgen.util.config import Config

class TestConfig(TestCase):

	DATA_DIR = abspath(Path('..', 'data'))
	CONFIG_FILE= str(Path(DATA_DIR, 'config.test.ini'))
	config_obj = None

	def setUp(self):
		self.config_obj = Config(self.CONFIG_FILE)

	def tearDown(self):
		self.config_obj = None

	def test_should_get_height_from_config(self):
		self.assertEqual(720, self.config_obj.get_height())

	def test_should_get_width_from_config(self):
		self.assertEqual(1080, self.config_obj.get_width())

