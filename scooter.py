from utilities import print_slow
class Player:
    def __init__(self):
        self.in_hand = {
            'money': 0,
            'breakfast': False,
            'backpack': [],
            'frog_power': False,
        }
player = Player()

def scooter():
    print("""Unfortunatly, in your hast, you forgot to grab anything useful and you are now locked out of your house with no keys and no wallet. You search around for anything with wheels that will get you to school as fast as possible. But the only thing you can find is your little sister's My Little Pony scooter. Do you:
    \n1. Take the scooter and risk dishonor on you, your' family and your' cow by someone seeing you?
    \n2. Give up on life and question every decision that has lead you to this moment?\n""")

    choice = int(input('Whatchu wanna do? '))
    if choice == 1:
        start_ride()
    elif choice == 2:
        print('GAME OVER')
    else:
        choice = int(input('Not valid. Enter 1 or 2 '))



def start_ride():
    print("""You are now riding at top speed down the road, and you are actually making pretty good time; you might actually make it to school on time. But while you were reveling in your sweet scooter skills, you crash into an old lady waiting for the bus. What do you do?
    \n1. Aplogize profusely and help her up.
    \n2. Keep on ridin baby! She may have broken her hip, but you have more important things going on right now.\n""")

    choice = int(input("What's it gonna be hotshot?"))

    if choice == 1:
        frog()
    elif choice == 2:
         not_frog()


def frog():
    print_slow("""You have decided that you should probably help the old lady up. So you stop and as you walk over to her, you can hear her talking in some strange language,"maybe she is foreign" you think to yourself {print} POOF all of a sudden things seem really big and you have developed a taste for flies. SHE TURNED YOU INTO A FROG!!! What do you do?
    \n1. Plead with the witch to turn you back and hope she takes pity on your soul.
    \n2. Get angry and try to take her down.
    \n3. Give into you craving for flies and try to find a pond somewhere.\n""")

    choice = int(input("What RIBBIT are RIBBIT you RIBBIT gonna RIBBIT do? "))

    if choice == 1:
        player.in_hand['frog_power'] = True
        print(player.in_hand['frog_power'])
        # super_powered()
    elif choice == 2:
        print(2)
    elif choice == 3:
        print(3)


def not_frog():
    print("""You continue to race down the side walk, you probably should have stopped but she seemed a little sketchy anyway.... So you're cuising down the sidewalk""")










scooter()
