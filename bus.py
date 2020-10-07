from utilities import print_slow

class Player:
    def __init__(self):
        self.in_hand = {
            'money': 25,
            'breakfast': True,
            'backpack': [],
        }
player = Player()
def bus():
    print('You chose to take the bus')
    print("""Luckily, the bus shows up at the bus stop one minute late and you are able to make it on the bus.
With your breakfast in hand, backpack on your back, and your wallet in your pocket,
you pay the bus driver $1 and look for a seat.\n
There are two open seats:\n
1. One on the second row next to what looks to be a 14 year old highschool kid.\n
2. Another near the back next to a sweet old lady with a big purse.\n\n
'Which seat do you choose? 1 or 2? '""")
    player.in_hand['money'] = 24
    seat_choice = int(input())

    if seat_choice == 1:
        print("""You sit down next to the kid and begin eating your breakfast. 5 minutes later the bus stops and picks up a pregnant woman. Do you give her your seat? Y or N? """)
        pregnant_choice = input().upper()
        if pregnant_choice == 'Y':
            print('You offer the pregnant woman your seat')
        elif pregnant_choice == 'N':
            print('You look down and avoid eye contact')

    elif seat_choice == 2:
        print('choice 2')

bus()
