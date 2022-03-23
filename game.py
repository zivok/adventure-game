import time;

""" description """
print ("You find yourself standing in an open field, "
+ "filled with grass and yellow wildflowers.")
time.sleep(2)

print ("Rumor has it that a wicked fairie is somewhere " 
+ "around here, and has been terrifying the nearby village.")
time.sleep(2)

""" choice """
print ("Enter 1 to knock on the door of the house.")
time.sleep(2)

print ("Enter 2 to peer into the cave.")
time.sleep(2)

print ("What would you like to do?")
time.sleep(2)

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

