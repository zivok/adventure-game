import time
import random

from click import option;

""" start actions """

def house(items, enemy, lives):
    environmentDescription = [
        "You approach the door of the house.",
        f"You are about to knock when the door opens and out steps a {enemy}.",
        f"Eep! This is the {enemy}'s house!",
        f"The {enemy} attacks you!"
    ]
    showCompose(environmentDescription)
    option = read("Would you like to (1) fight or (2) run away? ", [1, 2]);
    [fight, run][option](items, enemy, lives)


def cave(items, enemy, lives):
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
    option = read("(Please enter 1 or 2.) ", [1, 2])
    [house, cave][option](items, enemy, lives)
    

def fight(items, enemy, lives):

    if "Sword of Ogoroth" in items:
        environmentDescription = [
            f"As the {enemy} moves to attack, you unsheath your new sword.",
            "The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.",
            f"But the {enemy} takes one look at your shiny new toy and runs away!",
            f"You have rid the town of the {enemy}."
        ]
    else:
        environmentDescription = [
            "You do your best...",
            f"but your dagger is no match for the {enemy}."
        ]
        lives -= 1
    showCompose(environmentDescription)


def run(items, enemy, lives):
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

    option = read("(Please enter 1 or 2.) ", [1, 2])
    [house, cave][option](items, enemy, lives)


""" end actions """

def show(message):
    print (message)
    time.sleep(2)


def showCompose(messageList):
    for msg in messageList:
        show(msg)


def read(message, optionList):
    option = int(input(message))
    if option in optionList:
        return option - 1
    else:
        return read(message, optionList)


def wellcome(items, enemy, lives):
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
    option = read("(Please enter 1 or 2.) ", [1, 2])
    [house, cave][option](items, enemy, lives)


def gameover(lives):
    if lives == 0:
        show("You have been defeated!")
    else:
        show("You are victorious!")


def play():
    lives = 1
    items = []
    enemies = ["wicked fairie", "troll", "dragon", "gorgon", "pirate"]
    enemy = random.choice(enemies)
    wellcome(items, enemy, lives)
    gameover(lives)


play()