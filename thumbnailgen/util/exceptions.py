class NotImplementedException(Exception):
    def __init__(self):
        super().__init__('definition not implemented')
