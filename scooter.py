from utilities import print_slow, print_slower
class Player:
    def __init__(self):
        self.in_hand = {
            'money': 0,
            'breakfast': False,
            'backpack': ['calculator', 'math book', 'old gym socks'],
            'frog_power': False,
        }
player = Player()

def scooter():

    print("""Unfortunatly, in your hast, you forgot to grab anything useful and you are now locked out of your house with no keys and no wallet. You search around for anything with wheels that will get you to school as fast as possible. But the only thing you can find is your little sister's My Little Pony scooter. Do you:
    \n1. Take the scooter and risk dishonor on you, your family and your cow by someone seeing you?
    \n2. Give up on life and question every decision that has lead you to this moment?
    \nWhatchu wanna do? """)

    choice = int(input())
    if choice == 1:
        start_ride()
    elif choice == 2:
        print('GAME OVER')
    else:
        choice = int(input('Not valid. Enter 1 or 2 '))



def start_ride():
    print("""You are now riding at top speed down the road, and you are actually making pretty good time; you might actually make it to school on time. But while you were reveling in your sweet scooter skills, you crash into an old lady waiting for the bus. What do you do?
    \n1. Aplogize profusely and help her up.
    \n2. Keep on ridin baby! She may have broken her hip, but you have more important things going on right now.
    \nWhat's it gonna be hotshot? """)

    choice = int(input())

    if choice == 1:
        frog()
    elif choice == 2:
        player.in_hand['backpack'].append('sketchy bag')
        print(player.in_hand['backpack'])
        not_frog()


def frog():
    print("""You have decided that you should probably help the old lady up. So you stop, and as you walk over to her, you can hear her talking in some strange language,"maybe she is foreign" you think to yourself""")
    print_slower('...')
    print(""" POOF\n""")
    print("""           .--._.--.
          ( O     O )
          /   . .   \\
         .`._______.'.
        /(           )\\
      _/  \  \   /  /  \_
   .~   `  \  \ /  /  '   ~.
  {    -.   \  V  /   .-    }
_ _`.    \  |  |  |  /    .'_ _
>_       _} |  |  | {_       _<
 /. - ~ ,_-'  .^.  `-_, ~ - .\\
         '-'|/   \|`-`""")
    print("""\nSHE TURNED YOU INTO A FROG!!! What do you do?
    \n1. Plead with the old lady to turn you back and hope she takes pity on your soul.
    \n2. Get angry and try to take her down.
    \n3. Give into you craving for flies and try to find a pond somewhere.
    \nWhat RIBBIT are RIBBIT you RIBBIT gonna RIBBIT do? """)

    choice = int(input())

    if choice == 1:
        super_powered()
    elif choice == 2:
        mistake()
    elif choice == 3:
        enlightenment()


def enlightenment():
    print("""Food really is the most important thing in life. So you hop on into a near by forest and search for a pond with a nice supply of flies. Eventually you come to a small secluded pond and decide this is it.
    You are now at peace with life, sitting on your lilypad and eating flies to your hearts content. You have acheived enlightenment.""")


def mistake():
    print_slow("""You gather all of your strength and anger and power for one massive attack! You pounce AND""")
    print_slower('...')
    print_slow("""You bounce right off because you are a frog. At this point you decide that its time for plan B and you grovle at her feet.\n""")
    super_powered()

def super_powered():
    print("""The old lady reconsiders her decision; after all, you were going to help her up. She turns you back into a human and she tells you that you can now change into a frog at will. What next?
    \n1. Thank the lady for your new super power and get your butt to school.
    \n2. Become "FROG MAN! Archnemesis of the evil Fly Lord"
    \n What are you going to do? Remember, with great power come great responsibility. """)

    choice = int(input())
    if choice == 1:
        get_your_butt_to_school()
    elif choice == 2:
        adventure_of_frogman()


def adventure_of_frogman():
    print_slower('.....')
    print_slow("""15 years have passed. The world has been torn apart in the fight against the Fly Lord. But thankfully the humans had FROG MAN to lead them against Fly Lord and his army of fly zombies. Fly Lord was eventually defeated and the human race is eternally greatful that you made the decision on that fateful day to take up the mantel of FROG MAN.""")


def get_your_butt_to_school():
    print("""You finally make it to school, with just a couple minutes to spare. You run up the steps""")
    dragon()


def not_frog():
    print("""You continue to race to school, you probably should have stopped but she seemed a little sketchy anyway""")
    print_slower('...')
    print("""\nSo you're cuising down the sidewalk, not a care in the world, and you decide that you have a little extra time to grab some food. So you roll up to your favorite restaurant and order. But as you go to pay for it, you check in your backpack for your wallet which of course isn't there, but you do find a strange little bag full of dust that must have fallen into your bag when you hit the old lady. What do you do?
    \n1. Grab the food and run!
    \n2. Be honest and tell the cashier you forgot your wallet.
    \nWhat would your mother do? """)

    choice = int(input())

    if choice == 1:
        grab_food()
    elif choice == 2:
        be_honest()

def grab_food():
    player.in_hand['breakfast'] = True
    print("""You grab the food and hightail it out of there! You feel a little bad about it, but you were super hungry so oh well.
    You continue to ride your scooter and finally arrive at school.""")
    dragon()







def dragon():

    print_slower("""\n...\n......""")
    print_slow("""\nand then A DRAGON COMES FROM THE SKY BREATHING FIRE!!\n You did NOT see that coming!""")
    print_slower('   \n')
    print("""                                                     /===-
                                                    /===-_---~~~~~~~~~------____
                                                   |===-~___                _,-' `
                     -==\\\                          `//~\\\   ~~~~`---.___.-~~
                 ______-==|                         | |  \\\           _-~`
           __--~~~  ,-/-==\\\                        | |   `\\        ,'
        _-~       /'    |  \\\        ^     /\         / /      \\      /
      .'        /       |   \\\      /~\___/~~\   /' /        \\   /'
     /  ____  /         |    \`\.__/-~~   \  |_/'  /          \\/'
    /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                      \_|      /        _) | ;  ),   __--~~
                        '~~--_/      _-~/- |/ \   '-~ \\
                       {\__--_/}    / \\\_>-|)<__\\      \\
                       /'   (_/  _-~  | |__>--<__|      |
                      |   _/) )-~     | |__>--<__|      |
                      / /~ ,_/       / /__>---<__/      |
                     o-o _//        /-~_>---<__-~      /
                     (^(~          /~_>---<__-      _-~
                    ,/|           /__>--<__/     _-~
                 ,//('(          |__>--<__|     /  -Alex Wargacki  .----_
                ( ( '))          |__>--<__|    |                 /' _---_~\\
             `-)) )) (           |__>--<__|    |               /'  /     ~\\`\\
            ,/,'//( (             \\__>--<__\\    \            /'  //        ||
          ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
        `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
      ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
       ;'( ')/ ,)(                              ~~~~~~~~~~
      ' ') '( (/
        '   '  `""")
    print_slow("""\nWhat do you do?
    \n1. Give the dragon your breakfast and hope that's enough to let you go.
    \n2. Check your backpack to see if there is anything in there that might help.
    \n3. Use your frog powers to attack the dragon.
    \n4. Sit with the dragon and talk about your feelings.""")

    choice = int(input())

    if choice == 1:
        print_slow("""Are you sure you want to give the dragon your breakfast? Y or N? """)
        breakfast_choice = input().upper()

        if breakfast_choice == Y:
            print_slow("""Are you sure you really sure? Y or N? """)
            breakfast_choice2 = input().upper()

            if breakfast_choice2 == Y:
                print_slow("The dragon eats your breakfast and is satisfied. He let's you pass. You walk into school hungry, but victorious. You win!")
            elif breakfast_choice2 == N:
                print_slow("You will NEVER give up your breakfast! It's the most important meal of the day!\nThe dragon respects your decision, but he too is hungry and decides to follow the same philosophy. You are eaten.\nYOU LOSE")

        elif breakfast_choice == N:
            print_slow("You will NEVER give up your breakfast! It's the most important meal of the day!\nThe dragon respects your decision, but he too is hungry and decides to follow the same philosophy. You are eaten.\nYOU LOSE")

    elif choice == 2:
        print_slow("Your backpack contains:\n")
        iter()

    elif choice == 3:

        if player.in_hand['frog_power']:
            print_slow("You turn into a frog and to your great surprise, the dragon is deathly afraid of frogs and flies away screaming like a baby. You walk into school victorious. You win!")
        else:
            print_slow("Unfortunatly you are only a regular human being and have no frog powers. The dragon is a little confused but still eats you.\nYOU LOSE")

    elif choice == 4:
        print_slow("You sit and talk with the dragon for a little while, you talk with him about all the struggles and prejudices he has faced throughout his life, just for being a dragon. You are really making progress with him, and he is calming down.")
        print_slower("...")
        print_slow("But wait, this is a dragon and you aren't a certified therapist. So you didn't really fix his problems and he eats you.\nYOU LOSE")

def iter():
    index = 1
    for i in player.in_hand['backpack']:
        print(index,". ",i, "\n")
        index += 1
