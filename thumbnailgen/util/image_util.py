from PIL import Image
from os.path import exists, abspath, isabs


def cutoff_width(file: str, val: int):
    file = file if isabs(file) else abspath(file)
    img: Image = Image.open(file)

    width, height = img.size
    img = img.crop((0, 0, width-val, height))
    img.save(file)