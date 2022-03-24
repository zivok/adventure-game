import time
import random

from click import option;

""" start actions """

def goHouse(settings):
    enemy = settings["enemy"]
    environmentDescription = [
        "You approach the door of the house.",
        f"You are about to knock when the door opens and out steps a {enemy}.",
        f"Eep! This is the {enemy}'s house!",
        f"The {enemy} attacks you!"
    ]
    showCompose(environmentDescription)
    actions = {
        1: fight,
        2: run
    }
    actionSelector("Would you like to (1) fight or (2) run away? ", actions, settings);


def goCave(settings):
    items = settings["items"]
    environmentDescription = [
        "You peer cautiously into the cave.",
        "It turns out to be only a very small cave."
    ]

    if "Sword of Ogoroth" in items:
        environmentDescription += [
            "You've been here before, and gotten all the good stuff. It's just an empty cave now."
        ]
    else: 
        environmentDescription += [
            "Your eye catches a glint of metal behind a rock.",
            "You have found the magical Sword of Ogoroth!",
            "You discard your silly old dagger and take the sword with you."
        ]
        items.append("Sword of Ogoroth")
    
    environmentDescription += ["You walk back out to the field."]
    showCompose(environmentDescription)

    optionDescription = [
        "Enter 1 to knock on the door of the house.",
        "Enter 2 to peer into the cave.",
        "What would you like to do?"
    ]
    showCompose(optionDescription)

    actions = {
        1: goHouse,
        2: goCave
    }
    actionSelector("(Please enter 1 or 2.) ", actions, settings)


def fight(settings):
    enemy = settings["enemy"]
    if "Sword of Ogoroth" in settings["items"]:
        environmentDescription = [
            f"As the {enemy} moves to attack, you unsheath your new sword.",
            "The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.",
            f"But the {enemy} takes one look at your shiny new toy and runs away!",
            f"You have rid the town of the {enemy}.",
            "You are victorious!"
        ]
    else:
        environmentDescription = [
            "You do your best...",
            f"but your dagger is no match for the {enemy}.",
            "You have been defeated!"
        ]
        settings["alive"] = False
    showCompose(environmentDescription)


def run(settings):
    environmentDescription = [
        "You run back into the field. Luckily, you don't seem to have been followed."
    ]
    showCompose(environmentDescription)
    optionDescription = [
        "Enter 1 to knock on the door of the house.",
        "Enter 2 to peer into the cave.",
        "What would you like to do?"
    ]
    showCompose(optionDescription)

    actions = {
        1: goHouse,
        2: goCave
    }
    actionSelector("(Please enter 1 or 2.) ", actions, settings)


""" end actions """

def show(message):
    print (message)
    time.sleep(DELAY)


def showCompose(messageList):
    for msg in messageList:
        show(msg)


def readInt(message, optionList):
    option = int(input(message))
    if option in optionList:
        return option
    else:
        return readInt(message, optionList)


def actionSelector(message, actions, settings):
    option = readInt(message, list(actions.keys()))
    actions[option](settings)
    

def start(settings):
    environmentDescription = [
        "You find yourself standing in an open field, "
        "filled with grass and yellow wildflowers.",
        "Rumor has it that a wicked fairie is somewhere "
        "around here, and has been terrifying the nearby village."
    ]
    optionDescription = [
        "Enter 1 to knock on the door of the house.",
        "Enter 2 to peer into the cave.",
        "What would you like to do?"
        ];
    showCompose(environmentDescription + optionDescription)
    actions = {
        1: goHouse,
        2: goCave
    }
    actionSelector("(Please enter 1 or 2.) ", actions, settings)


def gameover(settings):
    if settings["alive"]:
        show("You win! :)")
    else:
        show("You lose. :(")
    show("Game Over.")


def read(message, optionList):
    option = input(message).lower()
    if option in optionList:
        return option
    else:
        return read(message, optionList)


def readYesNot(message):
    optionList = ["y", "n"]
    option = read(message, optionList)
    return option == optionList[0]

DELAY = 0
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
        show("Goodbye.")


game()