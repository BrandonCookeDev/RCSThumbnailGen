from sys import argv
from thumbnailgen.util.config import Config
from thumbnailgen.models.singles_image import SinglesImage
from thumbnailgen.models.doubles_image import DoublesImage

config = Config()
if __name__ == '__main__':
    type = config.get_game_type()
    if type is None:
        raise Exception('game_type cannot be null in config file')

    if type.lower() == 'singles':
        SinglesImage.write_file_with_config()
    elif type.lower() == 'doubles':
        DoublesImage.write_file_with_config()
    else:
        raise Exception('unknown game type: {}'.format(type))

