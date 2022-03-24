import time
from config import *


def read(message, optionList):
    option = input(message).lower()
    if option in optionList:
        return option
    else:
        return read(message, optionList)


def readInt(message, optionList):
    option = int(input(message))
    if option in optionList:
        return option
    else:
        return readInt(message, optionList)


def show(message):
    print(message)
    time.sleep(DELAY)


def showCompose(messageList):
    for msg in messageList:
        show(msg)
