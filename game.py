import time;

""" start actions """
def house():
    show("Enter to the house")


def cave():
    show("Enter to the cave")

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


def choice(option, actionList):
    actionList[option]()


def wellcome():
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
    choice(option, [house, cave])


def play():
    wellcome()


play()