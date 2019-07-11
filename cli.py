import inquirer
from sys import argv

from thumbnailgen.models.game import Game
from thumbnailgen.models.player import Player
from thumbnailgen.models.singles_image import SinglesImage

USAGE = 'USAGE cli.py'


def ask_singles_questions():
    singles_questions = [
        inquirer.Text('p1_tag',
                      message='Player 1 Smash Tag?'),
        inquirer.Text('p1_character',
                      message='Player 1 Character?'),
        inquirer.Text('p1_color',
                      message='Player 1 Color?'),
        inquirer.Text('p2_tag',
                      message='Player 2 Smash Tag?'),
        inquirer.Text('p2_character',
                      message='Player 2 Character?'),
        inquirer.Text('p2_color',
                      message='Player 2 Color?')
    ]
    return inquirer.prompt(singles_questions)


def ask_doubles_questions():
    doubles_questions = [
        inquirer.Text('p1_tag',
                      message='Player 1 Smash Tag?'),
        inquirer.Text('p1_character',
                      message='Player 1 Character?'),
        inquirer.Text('p1_color',
                      message='Player 1 Color?'),
        inquirer.Text('p2_tag',
                      message='Player 2 Smash Tag?'),
        inquirer.Text('p2_character',
                      message='Player 2 Character?'),
        inquirer.Text('p2_color',
                      message='Player 2 Color?'),
        inquirer.Text('p3_tag',
                      message='Player 3 Smash Tag?'),
        inquirer.Text('p3_character',
                      message='Player 3 Character?'),
        inquirer.Text('p3_color',
                      message='Player 3 Color?'),
        inquirer.Text('p4_tag',
                      message='Player 4 Smash Tag?'),
        inquirer.Text('p4_character',
                      message='Player 4 Character?'),
        inquirer.Text('p4_color',
                      message='Player 4 Color?')
    ]
    return inquirer.prompt(doubles_questions)


if __name__ == '__main__':
    questions = [
        inquirer.Text('background_image',
                      message='Url or local path to background image you wish to use?'),
        inquirer.Text('foreground_image',
                      message='Url or local path to foreground image you wish to use?'),
        inquirer.Text('logo_image',
                      message='Url or local path to logo image you wish to use?'),
        inquirer.Text('game_round',
                      message='What round of the tournament is this?'),
        inquirer.List('game_name',
                      message='What game is this for?',
                      choices=['Melee', 'Ultimate']),
        inquirer.List('game_type',
                      message='What type of thumbnail would you like to create?',
                      choices=['Singles', 'Doubles']),
    ]

    answers = inquirer.prompt(questions)
    print(answers)

    if answers['game_type'] is 'Singles':
        singles_answers = ask_singles_questions()

        game = Game(name=answers['game_name'], type=answers['game_type'], round=answers['game_round'])
        p1 = Player(tag=singles_answers['p1_tag'], character=singles_answers['p1_character'], color=singles_answers['p1_color'])
        p2 = Player(tag=singles_answers['p2_tag'], character=singles_answers['p2_character'], color=singles_answers['p2_color'])

        image = SinglesImage(
            height=1080,
            width=1920,
            background_image=answers['background_image'],
            foreground_image=answers['foreground_image'],
            logo_image=answers['logo_image'],
            game=game,
            player1=p1,
            player2=p2
        )

        image.write_file()
    else:
        doubles_answers = ask_doubles_questions()

