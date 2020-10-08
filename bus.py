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

    print('\nYou chose to take the bus\n')
    print("""  With your breakfast in hand, backpack on your back, and your wallet in your pocket, you get on the bus, pay the bus driver $1, and look for a seat.\n\n There are two open seats:\n 1. One on the second row next to a 14 year old highschool kid.\n 2. Another near the back next to a sweet old lady with a big purse.\n\n Which seat do you choose? 1 or 2? """)
    player.in_hand['money'] = 24

    #Choose your seat
    seat_choice = int(input())
    if seat_choice == 1:
        print("""\nYou sit down next to the kid and begin eating your breakfast. 5 minutes later the bus stops and picks up a pregnant woman. Do you give her your seat? Y or N? """)

        #Let the pregnant woman sit down?
        pregnant_choice = input().upper()
        if pregnant_choice == 'Y':
            print("""\nYou offer the pregnant woman your seat and she thanks you by giving you coupon for BOGO yogurt at Yogurt Mountain. Yay! You have 10 minutes to get to school.\n""")
            player.in_hand['backpack'].append('Yogurt Coupon')
            print("""\nEverything looks like you're going to make it on time...until the bus stops in its tracks. There's a Delorean sitting in the middle of the road blocking the bus. What?!\n\nDo you decide to: \n1. Wait on the bus until the Delorean is moved? or \n2. Take the Delorean for a spin?\n\n1 or 2? """)

            #Take the Delorean?
            delorean_choice = int(input())
            if delorean_choice == 1:
                print("It takes an hour for the Delorean to be moved. You didn't make it in time! You lost.\n")
            elif delorean_choice == 2:
                print("""You run off the bus and hop in the Delorean. It's out of fuel! You can either \n1. Use your breakfast as fuel for the Delorean. or \n2. Run as fast as you can to try to make it in time! """)

                #Fuel up the Delorean?
                fuel_choice = int(input())
                if fuel_choice == 1:
                    print('You pop open the Mr. Fusion reactor, throw your breakfast in, and start the engine. Here we go! You fly off toward school, park, and start walking in to school with 5 minutes to spare.\n')
                    player.in_hand['breakfast'] = False
                    print_slower("""\n...\n......""")
                    print_slow("""\nand then A DRAGON COMES FROM THE SKY BREATHING FIRE!!\n You did NOT see that coming!""")
                    print(f"""\n\nWhat should you do?!\nMaybe you can use something you have to get the dragon to go away.\n On hand, you have ${player.in_hand['money']} and {player.in_hand['backpack']}\n\nWhat do you want to offer the dragon?\n1. ${player.in_hand['money']}?\n2. {player.in_hand['backpack']}?\n1 or 2?""")

                    #Offer Dragon choice. End of game.
                    dragon_choice1 = int(input())
                    if dragon_choice1 == 1:
                        print(f"You offer the dragon the ${player.in_hand['money']}.\nIt's the dragon's birthday today and he is overwhelmed with gratitude for the gift! He flies away to go buy himself something gold.\n You have been victorious! You walk into school right on time!")
                    elif dragon_choice1 == 2:
                        print(f"You offer the dragon the {player.in_hand['backpack']}. The dragon is lactose intolerant and is insulted at the offer. He burns you to a crisp and you do not make it to school on time. You lose!")

                elif fuel_choice == 2:
                    print("You choose to run for it! But halfway there you realize you won't make it in time. You are sad. \n You give up and decide to go use your yogurt coupon and eat 2 bowls of yogurt by yourself as you wallow in failure.")

        elif pregnant_choice == 'N':
            print('\nYou look down and avoid eye contact')

    elif seat_choice == 2:
        print('choice 2')

bus()
