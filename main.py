import sys,time,random

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print_slow("Type whatever you want here")

#
#
#
# class Student_1:
#     in_hand = { money: '$25', keys: True, breakfast: True }
#
# class Student_2:
#     in_hand = { money: '$25', keys: True, breakfast: False }
#
# class Student_3:
#     in_hand = {None}
