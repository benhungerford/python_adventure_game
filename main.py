import random
import player
from utilities import print_slow, print_slower
import scooter
import delorean
import bus



def game():
    print("""\033[1;37;40m
    ____             __      __           _____      __                __
   / __ )____ ______/ /__   / /_____     / ___/_____/ /_  ____  ____  / /
  / __  / __ `/ ___/ //_/  / __/ __ \    \__ \/ ___/ __ \/ __ \/ __ \/ /
 / /_/ / /_/ / /__/ ,<    / /_/ /_/ /   ___/ / /__/ / / / /_/ / /_/ / /
/_____/\__,_/\___/_/|_|   \__/\____/   /____/\___/_/ /_/\____/\____/_/

    """)
    print_slow("""The sun peaks through the window. You feel peaceful and calm as you open your eyes and look over at your clock. It's 8:30am. "OH ^$&*, I'm gonna be late for school!", you say out loud.
    \n\nYou have an incredibly crucial decision to make. Do you:
    \n1. Calmly get up, get dressed, collect your things, make breakfast, and walk out the door?
    \n2. Frantically grab everything and run out the front door?
    \n3. Orrrrrrrrr...hear me out...just go back to bed man. Sleep was much better than all the stress.\n""")

    choice = int(input('Whatchu wanna do? 1, 2, or 3? '))

    if choice == 1:
        print_slow("""It took you 15 minutes to get ready to go, you now have 15 minutes to get to school on time.
        \nYou have 2 options: \n1. Take the bus. \n2. Take the Delorean\n""")
        vehicle_choice = int(input('1 or 2? '))
        if vehicle_choice == 1:
            bus.bus()
        if vehicle_choice == 2:
            restart = delorean.delorean()
            if restart:
                game()
    elif choice == 2:
        scooter.scooter()
    elif choice == 3:
        print('You fail at life. Game over.')

game()
