import time;

def show(message):
    print (message)
    time.sleep(2)

""" description """
show("You find yourself standing in an open field, "
+ "filled with grass and yellow wildflowers.")

show("Rumor has it that a wicked fairie is somewhere " 
+ "around here, and has been terrifying the nearby village.")

""" choice """
show("Enter 1 to knock on the door of the house.")

show("Enter 2 to peer into the cave.")

show("What would you like to do?")

while True:
    choice = input("(Please enter 1 or 2).")

    if choice == "1":
        print ("option 1")
        break
    elif choice == "2":
        print ("option 2")
        break
    else:
        print ("invalid option")

