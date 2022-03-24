import random
import console
from actions import start


def readYesNot(message):
    optionList = ["y", "n"]
    option = console.read(message, optionList)
    return option == optionList[0]


def gameover(settings):
    if settings["alive"]:
        console.show("You win! :)")
    else:
        console.show("You lose. :(")
    console.show("Game Over.")


def game():
    enemies = ["wicked fairie", "troll", "dragon", "gorgon", "pirate"]
    settings = {
        "alive": True,
        "items": [],
        "enemy": random.choice(enemies)
    }
    start(settings)
    gameover(settings)
    if readYesNot("Would you like to play again? (y/n) "):
        game()
    else:
        console.show("Goodbye.")


game()
