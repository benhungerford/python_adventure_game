from utilities import print_slow
from utilities import print_slower
from utilities import dragon_pic1

class Player:
    def __init__(self):
        self.in_hand = {
            'money': 25,
            'breakfast_burrito': True,
            'backpack': ["hover_board", "sports_almanac", "gum"],
        }

def delorean():
#choose to drive or fly delorean.....................................................
    print("""                      ___..............._
             __.. ' _'.""""""\\""""""""- .`-._
 ______.-'         (_) |      \\           ` \\`-. _
/_       --------------'-------\\---....______\\__`.`  -..___
| T      _.----._           Xxx|x...           |          _.._`--. _
| |    .' ..--.. `.         XXX|XXXXXXXXXxx==  |       .'.---..`.     -._
\_j   /  /  __  \  \        XXX|XXXXXXXXXXX==  |      / /  __  \ \        `-.
 _|  |  |  /  \  |  |       XXX|""'            |     / |  /  \  | |          |
|__\_j  |  \__/  |  L__________|_______________|_____j |  \__/  | L__________J
     `'\ \      / ./__________________________________\ \      / /___________\
        `.`----'.'   dp                                `.`----'.'
      `""""'                                         `""""'""")
    print_slow("""Roads...?!?!?  Where we're going, we don't need roads. \n
This is heavy...,  there is only 15 minutes left to get to school.. \n
    Which way to take? \n
    1. The highway \n
    2. The skyway \n \n
    Choose: 1 or 2 """)

    drivefly_choice = int(input())
#driving on the road is chosen here...................................................................
    if drivefly_choice == 1:
        print_slow("""You spend 5 minutes throwing all your trash in the delorean fuel cell,
then make like a tree and get out of here!\n  """)
#a choice to speed to school or drive the speed limit here.....................................................
        print_slow("""With only 10 minutes left you are in a race against time no doubt.
Do you speed down the highway? y or n: """)

        road_choice = input().lower()
#choosing not to speed here which ends the game immediately...............................
        if road_choice == "n":
            print_slow("""You're driving the freaking Delorean for crying out loud
and you don't want to drive fast???   Get out of my game.""")

#choosing to speed here. and running into traffic jam options.................................................................
        elif road_choice == "y":
            print_slow("""You push the pedal to the metal leaving tire marks in the driveway
and your worries behind.  Adrenaline rushing you fly down the road passing every obstacle in your way.
All of a sudden you see a traffic jam ahead \n
and luckily it's right at the interstate on ramp. Do you try to \n
1)- continue on the road and see if you can get through the traffic jam... or \n
2)- do you make a detour and get on the interstate?? \n
    1 or 2: """)
            traffic_choice = int(input())
            if traffic_choice == 1:
                print_slow("""You get to the traffic jam and try to get around it hoping to get through.  But you see there is
a wreck way up a ahead and it doesn't look good.  Do you  \n
    a)- wait patiently and hope it will magically clear up \n
    or \n
    b)- grab the hover board that's in the floor board and ditch the delorean?? \n
    a or b: """)

                wreck_choice = input()
#choosing to sit in traffic jam and wait...............................................................................
                if wreck_choice == "a":
                    print_slow("""You sit patiently waiting for traffic to clear up ahead and unfortunately it does not.
You end up being stuck there for 3 1/2 hours.  You never make it to school.  Game Over!!""")
#choosing to ditch the delorean for on hover board route........................................
                elif wreck_choice == "b":
                    print_slow(f"""You grab the hover board and ditch the delorean.  Placing the hover board under your feet,
you begin hovering through traffic getting all the way through until its clear.  As you get out of traffic you think you hear someone in the
background talking crazy....  something, something... dragon???  It was faint so clearly you miss heard.  Then
you grab hold on to the back of a jeep that has also just cleared the traffic jam.  The jeep has a student parking
sticker to your school on the back of it.  So you hover from the back of the jeep all the way to the school parking lot. As you get there you hear this loud noise
...  ...\n ......\n{dragon_pic1()}\nand then A DRAGON COMES FROM THE SKY BREATHING FIRE!!\n You did NOT see that coming! As the dragon lands you
let go of the jeep.  The jeep driver stops in a panic and the dragon starts to breath fire on the jeep.  The driver jumps out and tries
to run while the jeeps is melted and burnt to a crisp, but the dragon is so fast it chomps him up in a flash.   He never had a chance.  The dragon turns
and looks at you.    What do you do? \n
1- stand still and hope it leaves? \n
2- run... ? \n
3- fight ? \n
1,2 or 3:  """)

                    fight_choice = int(input())
                    if fight_choice == 1:
                        print_slow("""You stand still hoping that the dragons eyes are like a T-rex, If you don't move maybe
it won't see you.   But thats not the case.  It does see you and it shoots the hottest fire ever shot
leaving you a pile of ash in the parking lot.  YOU DIED!  Game Over""")

                    if fight_choice == 2:
                        print_slow("""You turn and run as fast as you can.  If you were on a football field you would be leaving all the
players in the dust, but the dragon is much faster.  It smashes you with its tail knocking you across the parking lot.  You can't
move anymore.  You just lay there hurt as the dragon walks up to you and swallows you whole.  \n
YOU DIED.  Game Over! """)

                    if fight_choice == 3:
                        print_slow("""You scream at it like a beast charging the dragon.  It begins to charge back.  As it gets you, it  starts to shoot fire.  You
throw down the hover board and jump on it hovering  quickly under the dragon before it is able to hit you.  It turns around quickly and begins
trying to slice you with its sharp tail.  But you dodge it and move all around avoiding the dragons strikes.  Then it smacks you with its claw
knocking you through the school building walls into the class you are late for.  Everyone is screaming from what is happening.  The dragon
crashes in the school coming after you and comes down to sink its teeth into you to finish you off and you move out of the way and it eats
one of the students instead.   You get up and see some chemical cleaner that says WARNING HIGHLY FLAMMABLE on it.  You pick it up and dump it all
over the hover board, then you see the that dragon is about to shoot fire again and just as it opens its mouth you throw the hover board up in its mouth and
when the fire starts to come out the hover board blows up killing the dragon.  Everyone cheers for you.  The school makes you a hero and gives a
terrific kid certificate and a excused tardy.  Your parents will be proud.   YOU WIN!!   """)

#this is the  option 2 of traffic choice.....................................................................................



            elif traffic_choice == 2:
                print_slow("""You stomp the gas pedal even harder avoiding the traffic jam speeding
your way down the on ramp and up the interstate. All of a sudden...
you see flashing lights in the rear view mirror.  WHAT!!!!!! Things just got heavier... \n
            A)- pull over \n
            or \n
            B)- wave good-bye to the cop and leave him behind \n
            a or b: """)



                cop_choice = input()
                if cop_choice == "a":
                    print_slow("""You pull over to the side of the highway.  Your adrenaline is rushing... your
 nerves are shot.... and you are sweating like crazy.   You now realize that the breakfast   burrito you ate
 this morning is not sitting well in your stomach.    Oh No Oh No... you are about to be sick on your stomach.
 Your stomach hurts so bad...., ughh... why is the officer taking so long.   do you...... \n
                    1 - try to sit and wait? \n
                    or \n
                    2- run for the bushes so you can take care of business?""")

                    stomach_choice = int(input())
                    if stomach_choice == 1:
                        print_slow("""You wait hoping you can hold yourself together.  The officer finally comes and you tell him you're
sick on your stomach and he lets you off with a warning and says its ok to speed to school for your emergency.
You pull out speeding off to school again.  You finally get to the school parking lot...""")
                        print_slower("""\n...\n......""")
                        dragon_pic1()
                        print_slow("""\nand then A DRAGON COMES FROM THE SKY BREATHING FIRE!!\n You did NOT see that coming!
You are already out of the car in a running panic to get to the bathroom when the dragon lands in front of
you to eat you and just as the dragon opens its mouth to swallow you whole, your body in a overly Adrenaline
panic releaves itself of your upset stomach pains.  Your pants become a dark brown color.  The dragon gets
a hint smell of you on the way down to eat you and immediately changes its mind and with a look of disgust, it flies
away.  You shamefully walk into school with 1 min left. You made it but you didn't win.""")

                    if stomach_choice == 2:
                        print_slow("""You can't hold it.  You bust out of the delorean in a frantic run running as fast as
you can towards the bushes.  Just as you get there you are tackled into the bushes.  The officer saw you
running and assummed you were trying to run away.  As you crash into the bushes the weight of the officer compresses
your body making you what you hoped was the biggest fart you've ever had, but unfortunately you just went to
the bathroom and turns out live pd was following him today and they have you doing that on live tv.  Needless to
say you won't be making it to school today.   Game Over """)


#;;;;;;;;;;;;this is if you choose to run from the cops option...........................

                if cop_choice == "b":
                    print_slow("""You stick your hand out of the window and wave goodbye to the officer and floor it... You keep going faster
and faster to get away from the officer not knowing you just topped 88 mph....   all of a sudden you are surrounded
by all this light and a loud thunder sound and suddenly you are driving in a field that was where the highway was
50 years ago.  What the...??   What to do... \n
                    1- speed up again and hope it takes you back to where you were? \n
                    2- use the sports_almanc to place some bets for the future before heading back? \n
                    3- see if you can find someone named Doc Brown to help you? \n
                    1, 2, or 3: """)

                    time_choice = int(input())
                    if time_choice == 1:
                        print_slow("""You speed back up in hopes of going back to the future.  You begin traveling back through time and end right
back at the beginning of the morning where you began.""")
                        return True
                    if time_choice == 2:
                        print_slow("""You drive out to vegas to place some big bets.  While you are inside making bets someone steals the
delorean.  You end up being stuck in the past for the rest of your life but...,  you have the sports almanac.
You are able to make yourself the most wealthiest and 'luckiest' person alive.  You live a good life.""")

                    if time_choice == 3:
                        print_slow("""You search the phone book for a Doctor Emmett Brown.  You tell him what happened and he agrees to help you.  He made an
adjustment to the flux capasitor to help you get back to the right moment.  You take off and the delorean takes you back to the
future to where you actually end up in the school parking lot with 5 mins to spare. CONGRATS YOU DID IT!!""")





#/////////if option 2 skyway is chosen.......////////////////////////////////////////////////////////////////








    elif drivefly_choice == 2:
        print_slow(""" You spend 5 minutes trying to figure out how to get the Delorean in flight mode, but you figure it out.
With only 10 minutes left, you shoot into the sky leaving the earth behind you.  You've never felt such a smooth ride.  You fly the
delorean so high and fast and you aren't even being bothered by g-force.  But all of a sudden you start hearing the Top Gun theme
song and you all of a sudden realize Maverick, Goose and Ice Man are on your six... you aren't suppose to be flying and they have been sent
to take you down...
what do you do?  \n
1- land the delorean \n
2- try to shake them \n
3-sing great balls of fire to them \n
1,2, or 3: """)

        sky_choice = int(input())
        if sky_choice == 1:
            print_slow("""You are afraid of being in trouble so you start to attempt to land the delorean.  You've never landed
the delorean before, and as you attempt to land it you loose control and crash into a mountain.  \n
YOU DIED!""")

        if sky_choice == 2:
            print_slow("""You stick your hand out the window and give them a thumbs down and speed off in hurry.
They begin shooting at you as you fly away.  Explosions are happening all around you as you try to avoid getting
hit by bullets and rockets.  One rocket blows up really close to you and some parts of the rocket fly through the window
destroying the flux capasitor.  The circuits in the delorean are sparking and the console catches on fire.
Just as you start to slow down to land and quit running Maverick flies over top of you upside down giving you the finger
and then drops a grenade in the delorean and blows you up.  YOU DIED!""")

        if sky_choice == 3:
            print_slow("""You begin singing Great Balls Of Fire as loud as you can.  As Maverick and Ice Man look puzzled, Goose shouts out
"THAT'S MY JAM" and starts singing along with you.  Even though Maverick and Ice Man are really confused right now they
can't resist the soul and good feelings from the song. Maverick starts bobbing his head and begins singing along too.  Ice Man also
starts singing but more quietly sings.  He doesn't really know this song i guess.  You guys become friends and they lead you to school.
You get there with 5 minutes to spare.  Congrats You Win.""")
