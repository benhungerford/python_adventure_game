from utilities import print_slow

class Player:
    def __init__(self):
        self.in_hand = {
            'money': 15,
            'breakfast_burrito': True,
            'hover_board': True,
            'backpack': [],
        }

def delorean():
#choose to drive or fly delorean.....................................................
    print("""Roads...?!?!?  Where we're going, we don't need roads. \n
This is heavy...,  there is only 15 minutes left to get to school.. \n
    Which way to take? \n
    1. The highway \n
    2. The skyway \n \n
    Choose: 1 or 2 """)

    drivefly_choice = int(input())
#driving on the road is chosen here...................................................................
    if drivefly_choice == 1:
        print("""You spend 5 minutes throwing all your trash in the delorean fuel cell,
then make like a tree and get out of here!\n  """)
#a choice to speed to school or drive the speed limit here.....................................................
        print("""With only 10 minutes left you are in a race against time no doubt.
    Do you speed down the highway? y or n: """)

        road_choice = input().lower()
#choosing not to speed here which ends the game immediately...............................
        if road_choice == "n":
                print("""You're driving the freaking Delorean for crying out loud
and you don't want to drive fast???   Get out of my game.""")

#choosing to speed here. and running into traffic jam options.................................................................
        elif road_choice == "y":
            print("""You push the pedal to the metal leaving tire marks in the driveway
and your worries behind.  Adrenaline rushing you fly down the road passing every obstacle in your way.
All of a sudden you see a traffic jam ahead \n
and luckily its right at the interstate on ramp. Do you try to \n
1)- continue on the road and see if you can get through the traffic jam... or \n
2)- do you make a detour and get on the interstate?? \n
    1 or 2: """)
            traffic_choice = int(input())
            if traffic_choice == 1:
                print("""You get to the traffic jam and try to get around it hoping to get through.  But you see there is
a wreck way up a ahead and it doesn't look good.  Do you  \n
    a)- wait patiently and hope it will magically clear up \n
    or \n
    b)- grab the hover board that's in the floor board and ditch the delorean?? \n
    a or b: """)

                wreck_choice = input()
#choosing to sit in traffic jam and wait...............................................................................
                if wreck_choice == "a":
                    print("""You sit patiently waiting for traffic to clear up ahead and unfortunately it does not.
You end up being stuck there for 3 1/2 hours.  You never make it to school.  Game Over!!""")
#choosing to ditch the delorean for on hover board route........................................
                elif wreck_choice == "b":
                        print("""You grab the hover board and ditch the delorean.  Placing the hover board under your feet,
you begin hovering through traffic getting all the way through until its clear.  As you get out of traffic you think you hear someone in the
background talking crazy....  something, something... dragon???  It was faint so clearly you miss heard.  Then
you grab hold on to the back of a jeep that has also just cleared the traffic jam.  The jeep has a student parking
sticker to your school on the back of it.  So you hover from the back of the jeep all the way to the school parking lot. """)
#this is the  option 2 of traffic choice.....................................................................................
            elif traffic_choice == 2:
                print("""You stomp the gas pedal even harder avoiding the traffic jam speeding
your way down the on ramp and up the interstate. All of a sudden...
you see flashing lights in the rear view mirror.  WHAT!!!!!! Things just got heavier... \n
            A)- pull over \n
            or \n
            B)- wave good-bye to the cop and leave him behind \n
            a or b: """)

                cop_choice = input()
                if cop_choice = "a"





#/////////if option 2 skyway is chosen.......///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
