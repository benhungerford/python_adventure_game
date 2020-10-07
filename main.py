import sys,time,random
import scooter
# import delorian
# import bus

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.06)

print("""The sun peaks through the window. You feel peaceful and calm as you open your eyes and look over at your clock. It's 8:30am. "OH ^$&*, I'm gonna be late for school!", you say out loud.
\n\nYou have an incredibly crucial decision to make. Do you:
\n1. Calmly get up, get dressed, collect your things, make breakfast, and walk out the door?
\n2. Frantically grab everything and run out the front door?
\n3. Orrrrrrrrr...hear me out...just go back to bed man. Sleep was much better than all the stress.\n""")

choice = int(input('Whatchu wanna do? '))

if choice == 1:
    scooter.scooter()

# if choice == 2:
#
# if choice == 3:

#
#
#
# class Student_1:
#     in_hand = { money: '$25', breakfast: True, backpack: []}
#
# class Student_2:
#     in_hand = { money: '$25', breakfast: False }
