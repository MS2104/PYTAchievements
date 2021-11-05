import time

# This variable makes sure you can close the game properly.
running = True

# Variables

clothing1 = "1. Red sweater + jeans"
clothing2 = "2. Suit"
clothing3 = "3. Black shirt & green cargo pants"

# Main questions

def firstchoicefunction():
    while True:
        print("It's 7AM, your alarm goes off.")
        print("Do you SNOOZE the alarm or WAKE UP?")
        
        firstchoice = input(">>> ")

        if firstchoice == 'SNOOZE':
            print('You snooze the alarm, and fall asleep.')
            time.sleep(3)
            print("You wake up 30 minutes later. It's 7:30, you're running late so you decide to get out of bed and put on your clothes")
            break
        elif firstchoice == 'WAKE UP':
            print("You decide to get out of bed.")
            break
        else:
            print(firstchoice, " wasn't a valid choice!")
            time.sleep(1)

def secondchoicefunction():
    while True:
        print("You walk into the bathroom and brush your teeth. Your hair looks like a mess. WALDo you put gel in your hair to style it or brush it?")

        secondchoice = input("gel/brush: ")

        if secondchoice == 'gel':
            print("You put in gel to make your hair look nice.")
            break
        elif secondchoice == 'brush':
            print("You brushed your hair so it looks alot less messier.")
            break
        else:
            print("That isn't a valid choice.")

def thirdchoicefunction():
    while True:
        print("It's time to get dressed, these are your options:")

        print(clothing1)
        print(clothing2)
        print(clothing3)

        print("You can pick between 1, 2 and 3.")

        secondchoice = input(">>> ")
        if secondchoice == '1':
            print("You put on your ", clothing1)
            break
        if secondchoice == '1':
            print("You put on your red sweater and jeans.")
            break
        elif secondchoice == '2':
            print("You decided you're going to wear your suit.")
            break
        elif secondchoice == '3':
            print("You put on your suit.")
            break
        else:
            print("You don't have that in your wardrobe!")

def fourthchoicefunction():
    while True:
        print("You head down stairs and into the kitchen to go make breakfast")
        print("You can pick between the following: ")
        print("CORNFLAKES, BREAD or OATMEAL")

        thirdchoice = input(">>> ")

        if thirdchoice == 'CORNFLAKES':
            print("You put some kelloggs in a bowl and poured milk, and ate it.")
            break
        elif thirdchoice == 'BREAD':
            print("You put some jam on bread and ate it.")
            break
        elif thirdchoice == 'OATMEAL':
            print("You made some oatmeal and ate it.")
            break
        else:
            print("You couldn't find", thirdchoice, 'in your kitchen.')

def fifthchoicefunction():
    while True:
        print("You're running late for work")
        print("You put on your shoes and head out to your car to get to work. Once you arrive at your car, you realize you forgot your keys.")
        print("Do you, A. Go back home to get your keys or B. go with the bus?")

        fourthchoice = input(">>> ")

        if fourthchoice == 'A' or 'a':
            print("You went back home to get your keys and came back to your car.")
            break
        elif fourthchoice == 'B' or 'b':
            break
        else:
            print("That's not a valid option!")

while running:
    firstchoicefunction()
    secondchoicefunction()
    thirdchoicefunction()
    fourthchoicefunction()
    fifthchoicefunction()
    print("DailyChoices.py by Milad Sahar")
    running = False