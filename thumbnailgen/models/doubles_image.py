from pathlib import Path

from thumbnailgen.models.image import Image
from thumbnailgen.util.common import get_web_dir


class DoublesImage(Image):

    def __init__(self, height, width, filename='doubles-thumbnail.html'):
        super().__init__(height, width)
        self.html_file = str(Path(get_web_dir(), filename))
