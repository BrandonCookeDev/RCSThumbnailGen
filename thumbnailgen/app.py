from sys import argv
from pathlib import Path
from thumbnailgen.util.config import Config
from thumbnailgen.models.singles_image import SinglesImage
from thumbnailgen.models.doubles_image import DoublesImage
from thumbnailgen.util.common import get_root_dir
from thumbnailgen.util.screenshoter import screenshot_file
from thumbnailgen.util.image_util import cutoff_width, \
    cutoff_height, convert_to_jpg, resize

config = Config()

if __name__ == '__main__':
    type = config.get_game_type()
    if type is None:
        raise Exception('game_type cannot be null in config file')

    if type.lower() == 'singles':
        html_output_location = SinglesImage.write_file_with_config()
        dest_image_location = str(Path(get_root_dir(), 'singles-thumbnail.png'))
        screenshot_file(html_output_location, dest_image_location)
        cutoff_width(dest_image_location, 1150)
        cutoff_height(dest_image_location, 300)
        resize(dest_image_location, 1290, 720)
        convert_to_jpg(dest_image_location, 90)
    elif type.lower() == 'doubles':
        DoublesImage.write_file_with_config()
    else:
        raise Exception('unknown game type: {}'.format(type))

