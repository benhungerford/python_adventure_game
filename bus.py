from utilities import print_slow
from utilities import print_slower

class Player:
    def __init__(self):
        self.in_hand = {
            'money': 25,
            'breakfast': True,
            'backpack': [],
        }
player = Player()
def bus():

    print_slow('\nYou chose to take the bus\n')
    print_slow("""  With your breakfast in hand, backpack on your back, and your wallet in your pocket, you get on the bus, pay the bus driver $1, and look for a seat.\n\n There are two open seats:\n 1. One on the second row next to a 14 year old highschool kid.\n 2. Another near the back next to a sweet old lady with a big purse.\n\n Which seat do you choose? 1 or 2? """)
    player.in_hand['money'] = 24

    #Choose your seat
    seat_choice = int(input())
    if seat_choice == 1:
        print_slow("""\nYou sit down next to the kid and begin eating your breakfast. 5 minutes later the bus stops and picks up a pregnant woman. Do you give her your seat? Y or N? """)

        #Let the pregnant woman sit down?
        pregnant_choice = input().upper()
        if pregnant_choice == 'Y':
            print_slow("""\nYou offer the pregnant woman your seat and she thanks you by giving you a coupon for BOGO yogurt at Yogurt Mountain. Yay! You have 10 minutes to get to school.\n""")
            player.in_hand['backpack'].append('Yogurt Coupon')
            print_slow("""\nEverything looks like you're going to make it on time...until the bus stops in its tracks. There's a Delorean sitting in the middle of the road blocking the bus. What?!\n\nDo you decide to: \n1. Wait on the bus until the Delorean is moved? or \n2. Take the Delorean for a spin?\n\n1 or 2? """)

            #Take the Delorean?
            delorean_choice = int(input())
            if delorean_choice == 1:
                print_slow("It takes an hour for the Delorean to be moved. You didn't make it in time! You lost.\n")
            elif delorean_choice == 2:
                print_slow("""You run off the bus and hop in the Delorean. It's out of fuel! You can either \n1. Use your breakfast as fuel for the Delorean. or \n2. Run as fast as you can to try to make it in time!\n\n1 or 2? """)

                #Fuel up the Delorean?
                fuel_choice = int(input())
                if fuel_choice == 1:
                    print_slow('You pop open the Mr. Fusion reactor, throw your breakfast in, and start the engine. Here we go! You fly off toward school, park, and start walking in to school with 5 minutes to spare.\n')
                    player.in_hand['breakfast'] = False
                    print_slower("""\n...\n......""")
                    print_slow("""\nand then A DRAGON COMES FROM THE SKY BREATHING FIRE!!\n You did NOT see that coming!""")
                    print_slow(f"""\n\nWhat should you do?!\nMaybe you can use something you have to get the dragon to go away.\n On hand, you have ${player.in_hand['money']} and {player.in_hand['backpack']}\n\nWhat do you want to offer the dragon?\n1. ${player.in_hand['money']}\n2. {player.in_hand['backpack']}\n1 or 2? """)

                    #Offer Dragon choice. End of game.
                    dragon_choice1 = int(input())
                    if dragon_choice1 == 1:
                        print_slow(f"You offer the dragon the ${player.in_hand['money']}.\nIt's the dragon's birthday today and he is overwhelmed with gratitude for the gift! He flies away to go buy himself something gold.\n You have been victorious! You walk into school right on time!")
                    elif dragon_choice1 == 2:
                        print_slow(f"You offer the dragon the {player.in_hand['backpack']}. The dragon is lactose intolerant and is insulted at the offer. He burns you to a crisp and you do not make it to school on time. You lose!")

                elif fuel_choice == 2:
                    print_slow("You choose to run for it! But halfway there you realize you won't make it in time. You are sad. \n You give up and decide to go use your yogurt coupon and eat 2 bowls of yogurt by yourself as you wallow in failure.")

        elif pregnant_choice == 'N':
            print_slow("""\nYou look down and avoid eye contact as the pregnant woman has to stand up.\nThe kid next to you decides to get off at the next stop. He bumps into you as he tries to get out, but now the pregnant woman has a place to sit. You feel awkward...do you:\n1. Decide to get off the bus as well? or\n2. Stay in your seat until you get to school?\n1 or 2? """)
            player.in_hand['money'] = 0

            #Sit next to the pregnant lady?
            exit_choice = int(input())
            if exit_choice == 1:
                print_slow("\nYou decide to get off the bus and get an Uber. That should get you to school faster than the bus anyway.\nAn Uber comes to pick you up, but you realize you have no money! That kid stole your wallet when he bumped into you. You can't make it in time. Oh no!\nYOU LOSE.")
            elif exit_choice == 2:
                print_slow("""You akwardly stay seated.\nAll of a sudden, the woman screams, "I NEED TO GO TO THE HOSPITAL! I'm about to have my baby!\nThe bus driver panics, stops the bus, and faints.\nIt's up to you to drive the bus! Do you decide to:\n1. Drive the bus to the hospital? or\n2. Drive the bus to school?""")

                #Drive bus to school or hospital?
                drive_choice = int(input())
                if drive_choice == 1:
                    print_slow("""You are valiant and drive the bus to the hospital! You're extremely late for school, but you become the child's godparent and you realize that sometimes doing what's right is more rewarding than doing what is urgent.\n\nYou still lose the game though.""")
                elif drive_choice == 2:
                    print_slow("""You don't have time for this! You drive to school, ignoring the painful screams of the woman. You park the bus as the woman is having her baby on the third row and another passenger is calling an ambulance. No one likes you. But hey, you're about to walk into school on time.""")
                    print_slower("""\n...\n......""")
                    print_slow("""\nand then A DRAGON COMES FROM THE SKY BREATHING FIRE!!\n You did NOT see that coming!""")
                    print_slow("You try to think of what you have on you to get the dragon to go away. You're missing your wallet...did that kid steal it from you?!\n All you have is your breakfast. Do you offer it to the dragon?\n Y or N?")

                    #Offer your breakfast? End of game
                    offer_choice = input().upper
                    if offer_choice == 'Y':
                        print_slow("The dragon is not hungry for your breakfast, he's hungry for you! You are eaten.\n YOU LOSE")
                    elif offer_choice == 'N':
                        print_slow("You don't want to give up your food, but you don't want to be eaten by the dragon either.\nThe dillema makes you break down in tears.\nThe dragon feels bad for you and let's you pass as long as you promise to make good grades and be nice to your friends.\nYou win!")



    elif seat_choice == 2:
        print_slow("\nAs you sit next to the old lady. She begins talking to you about how her hip hurts. As she talks, you are worried about being able to get out of the conversation before your stop. Do you:\n1. Interupt her and tell her that you don't care about her hip and you need to focus on getting to school on time? or\n2. Listen intently and offer emotional support?\n1 or 2? ")

        #Listen to the old lady?
        old_lady_choice = int(input())
        if old_lady_choice == 1:
            print_slow("\nThe lady is offended that you rudely interrupt her. All of a sudden, she turns you into a frog and puts you in her purse. It's dark, you're scared, and you don't think you'll make it to school on time.\nYOU LOSE")
        elif old_lady_choice == 2:
            print_slow("\nYou spend the next 10 minutes listening to her talk, all the while hoping you can still make it in time. You reach your stop and the old lady is so grateful that you listened that she offers you a caramel candy. You take it and walk off the bus.\nYou start walking toward the front door of the school with 5 minutes to spare.")
            player.in_hand['backpack'].append('Caramel Candy')
            print_slower("""\n...\n......""")
            print_slow("""\nand then A DRAGON COMES FROM THE SKY BREATHING FIRE!!\n You did NOT see that coming!""")
            print_slow(f"\nMaybe you can offer him something that you have to make him go away. Here's what you have in hand:\n1. ${player.in_hand['money']}\n2. {player.in_hand['backpack']}\n3. Your breakfast.\n\nWhat do you offer?\n1, 2, or 3? ")
            dragon_choice2 = int(input())
            if dragon_choice2 == 1:
                print_slow(f"\nYou offer the dragon the ${player.in_hand['money']}.\nIt's the dragon's birthday today and he is overwhelmed with gratitude for the gift! He flies away to go buy himself something gold.\n You have been victorious! You walk into school right on time!")
            elif dragon_choice2 == 2:
                print_slow(f"\nYou offer the dragon the {player.in_hand['backpack']}.\n He likes it! But it's not enough. You must offer him more.\nDo you give him your breakfast? Y or N?")
                breakfast_choice = input().upper()
                if breakfast_choice == 'Y':
                    print_slow("The dragon eats your breakfast and is satisfied. He let's you pass. You walk into school hungry, but victorious. You win!")
                elif breakfast_choice == 'N':
                    print_slow("You will NEVER give up your breakfast! It's the most important meal of the day!\nThe dragon respects your decision, but he too is hungry and decides to follow the same philosophy. You are eaten.\nYOU LOSE")
            elif dragon_choice2 == 3:
                print_slow("You relunctantly offer your breakfast. The dragon lets you live...for now. You walk into school on time.")
                print_slower('\n......\nuntil school ends and you walk outside...')

bus()
