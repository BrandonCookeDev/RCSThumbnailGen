from sys import argv
from thumbnailgen.models.singles_image import SinglesImage
from thumbnailgen.models.player import Player
from thumbnailgen.models.game import Game


if __name__ == '__main__':
    p1 = Player('Mango', 'Falco', 'Green')
    p2 = Player('PPMD', 'Falco', 'Blue')
    game = Game('MELEE', 'SINGLES', 'Pools')
    image = SinglesImage(
        background_image='../images/RecursionBackground.png',
        foreground_image='../images/1080p-Wallpapers-1.jpg',
        logo_image='../images/RecursionLogo.jpg',
        game=game,
        player1=p1,
        player2=p2
    )
    image.write_file()

