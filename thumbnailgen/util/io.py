from os.path import exists, abspath, isabs


def get_file_content(file: str) -> str:
    if not isabs(file):
        file = abspath(file)
    if not exists(file):
        raise Exception('file {} does not exists'.format(file))

    with open(file, 'r') as f:
        return f.read()
