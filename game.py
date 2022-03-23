import time

from click import option;

""" start actions """

def house(items):
    environmentDescription = [
        "You are about to knock when the door opens and out steps a troll.",
        "Eep! This is the troll's house!",
        "The troll attacks you!"
    ]
    showCompose(environmentDescription)
    option = read("Would you like to (1) fight or (2) run away?", [1, 2]);
    choice(option, [fight, run], items)


def cave(items):
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
    choice(option, [house, cave], items)
    

def fight(items):

    if "Sword of Ogoroth" in items:
        environmentDescription = [
            "As the troll moves to attack, you unsheath your new sword.",
            "The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.",
            "But the troll takes one look at your shiny new toy and runs away!",
            "You have rid the town of the troll.",
            "You are victorious!"
        ]
    else:
        environmentDescription = [
            "You do your best...",
            "but your dagger is no match for the troll.",
            "You have been defeated!"
        ]
    showCompose(environmentDescription)


def run(items):
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
    choice(option, [house, cave], items)


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


def choice(option, actionList, args):
    actionList[option](args)


def wellcome(items):
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
    choice(option, [house, cave], items)


def play():
    items = []
    wellcome(items)


play()