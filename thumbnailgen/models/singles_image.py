import json
from pathlib import Path

from thumbnailgen.models.image import Image
from thumbnailgen.util.common import get_web_dir


class SinglesImage(Image):

    def __init__(self, height, width, filename='singles-thumbnail.html'):
        super().__init__(height, width)
        self.html_file = str(Path(get_web_dir(), filename))

    def write_data(self):
        pass

    def draw(self):
        pass