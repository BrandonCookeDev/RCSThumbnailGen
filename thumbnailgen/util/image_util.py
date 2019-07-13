from PIL import Image
from pathlib import Path
from os.path import exists, abspath, isabs
from os import remove

from thumbnailgen.util.common import change_file_extension


def cutoff_width(file: str, val: int):
    file = file if isabs(file) else abspath(file)
    img: Image = Image.open(file)

    width, height = img.size
    img = img.crop((0, 0, width-val, height))
    img.save(file)


def cutoff_height(file: str, val: int):
    file = file if isabs(file) else abspath(file)
    img: Image = Image.open(file)

    width, height = img.size
    img = img.crop((0, 0, width, height-val))
    img.save(file)


def resize(file: str, width: int, height: int):
    file = file if isabs(file) else abspath(file)
    img: Image = Image.open(file)

    img = img.resize((width, height), Image.ANTIALIAS)
    img.save(file)


def convert_to_jpg(file: str, quality=95):
    file = file if isabs(file) else abspath(file)
    img: Image = Image.open(file)

    new_file_name = change_file_extension(file, '.jpg')

    remove(file)
    img = img.convert("RGB")
    img.save(new_file_name, quality=quality)
