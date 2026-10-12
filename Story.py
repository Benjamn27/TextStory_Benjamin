character = "null"

def bebop_picked():
    print("You've chosen Bebop, a fine choice")
    print("")
    character = "Bebop"
    new_york()

def ridely_picked():
    print("You've chosen Bebop, a fine choice")
    print("")
    character = "Ridely"
    the_Moon()

def cookie_monster_picked():
    print("You've chosen Cookie Monster, I hope it works out for you")
    print("")
    character = "Cookie Monster"
    the_underworld()

def not_heard():
    print("I didn't quite catch that, but I think you'd love to pick Bebop")
    print("")
    character = "Bebop"
    new_york()



def new_york():
    print("You find yourself in New York, a beautiful city, that is currently undergoing a ritual caused by two conflicting gods." \
    "You are fighting for the Allmother and you must choose what to do to gain power. You could defend your guradians, gaining souls from the opposing minions," \
    "you could farm in the jungle by killing the creeps, or you can hunt your opponents traveling through objectives.")
    powerChoice = input("(Defend/Farm/Hunt) ")

    if powerChoice.upper() == "DEFEND":
        defend_gurdian()
    elif powerChoice.upper() == "FARM":
        farm_creeps
    elif powerChoice.upper() == "HUNT":
        print("You go to hunt the followers of the Hidden King, but you quickly realize you are outnumbered. Haze, a sandman officer, notices you and alerts her teammates." \
        "You try to run away, but here sleep knife prevents you from getting far. You are swarmed, leaving only a pile of scrap.")
        print("")
        print("THE END")
    else:
        print("As you were about to go forward with your plan, the Allmother demands that you defend the gurdian, so you do.")
        print("")
        defend_gurdian()

def defend_gurdian():
    print("You are defending your gurdian, killing all the minions that try to destroy it, but Graves, a girl who commands the dead with the hand of a lich, opposes you." \
    "If you could take her out and eliminate the enemy gurdian, the ritual is as good as yours! You think about your abilities, deciding which could defeat this necromancer and" \
    "their army of zombies and floating skulls. Which do you pick?")
    gravesOption = input("(Punch/Bomb/Hook) ")

    if gravesOption.upper() == "HOOK":
        print("You ready your hook as the undead begin to advance. instead of aiming for the undead, you set your sights right on graves. You launch your hook, get a direct hit, and pull her in." \
        "She has no wave to protect her now, and with the combined power of you and your gurdian, you take Graves down. It was only a matter of time before you and the Allmother's minions crash through the Hidden Kings defences." \
        "The Allmother gives you one wish, which you use to cure your mother. You live peacefully with her on Long Island and retire your bombs and hook.")
        print("")
        print("THE END")
    elif gravesOption.upper() == "PUNCH":
        print("You arm your explosive punch and crash through the army of undead. You crack the skulls out of the sky and pound the zombies back ito the ground." \
        "Unforunatly for you, the waves keep coming, and with the next waves of minions coming in, you can make no advancements towards graves. You slowly are widdled down, dying in a blaze of glory.")
        print("")
        print("THE END")
    elif gravesOption.upper() == "BOMB":
        print("You ready your bombs and start putting them on every skull and zombie you can reach. bones are flying everywhere, the battlefield looks like a firework show." \
        "You keep on bombing the waves, but they keep coming. Your bombs slowly run out, leaving you stranded in the hole you've made as the undead pile atop you, making you one of them.")
        print("")
        print("THE END")
    else:
        print("As you begin to charge in, Mo and krill, a sewer dwelling duo, hands you down with their stunning combo, restricting all movement." \
        "The waves of undead crash on you and there is nothing you can do to spot them.")
        print("")
        print("THE END")

def farm_creeps():
    print("You have entered the jungle, the home of the many creeps of New York. You begin slaying all the creeps, gaining many souls and increasing your power." \
    "Suddenly, The Drifter appears, a blood thristy vampire who preys and those who are alone. If you kill him, your sould count will skyrocket, allowing you to sweep through the ritual." \
    "You must choose your strategy properly. If you don't he will surely kill you. How do you plan to slay the vampire?")
    drifterChoice = input("(Punch/Bomb/Laser)")

    if drifterChoice.upper() == "PUNCH":
        print("You start approaching The Drifter, ready to bust his skull open. You start throwing punches, but he avoids. You keep trying, but each try" \
        "only allows him to. The fight is long and hard, but you cannot outpace The Drifter, his years of battle outclass your robotic strategy." \
        "You eventually falter, allowing the drifter to land the finishing blow.")
        print("")
        print("THE END")
    elif drifterChoice.upper() == "BOMB":
        print("You ready your bombs and rush The Drifter. You know you won't be able to hit every bomb, so you focus on preventing his movements." \
        "You place bombs all around, forcing him to focus on multiple areas at once. One his mind wanders away from you, you land your finishing assault." \
        "The Drifter is defeated, and the ritual is as good as over. You defeat the Hidden King and save your mother.")
        print("")
        print("THE END")
    elif drifterChoice.upper() == "LASER":
        print("You ready your ultimate attack, a giant death laser, capable of destroying anything in its path. The downside is that aiming isn't very easy." \
        "The Drifter easily dodges your laser, almost playing with you. You try your hardest to reaim, but the energy needed to fire is took much. You collapse, and The Drift pounces on you.")
        print("")
        print("THE END")
    else:
        print("As you begin to approach him, you see movement in the corner of your eye. It was a trap. Sinclair, a magical puppet, casts a hex on you, turning you into a bunny." \
        "Your little fluffy body is helpless, allowing The Drifter to easily take your life.")
        print("")
        print("THE END")

def the_Moon():
    print("You find yourself on the moon, a barren wasteland at first glance, but you know there is bountiful treasure somewhere." \
    "You stumble upon a deep hole, so deep you can't see the bottom. You have brought lots of equiptment, a pirate is always prepared." \
    "What would you like to do?")
    holeChoice = input("(jump/Explode/Fill) ")

    if holeChoice.upper() == "JUMP":
        hole_jump()
    elif holeChoice.upper() == "EXPLODE":
        hole_explode()
    elif holeChoice.upper() == "Fill":
        print("You start filling the hole with surrounding rocks and other random objects you find. You throw in some moon dust, a random flag, a nintendo 64, but the hole is still not filled." \
        "You start throwing your own equitment into the hole to try to fill it up, but nothing happens. As a last resort, you fly your ship into the hole. It is far to big for the hole, but it does plug the hole." \
        "You triumphently dance, as you have beaten the hole. Sadly you now have nothing with you and your ship is ruined. You are forced to fly back home across the galaxy with no treasures.")
        print("")
        print("THE END")
    else:
        print("AS you were about to proceed with your masterful plan, a rabbit pushed you into the hole.")
        print("")
        hole_jump()

def hole_jump():
    print("You fall for a couple of seconds until you find yourself in a factory. Cheese is being transported all around and little rabbits are working the machines." \
    "You don't really want cheese, but there might still be something in this factory that could be worth the adventure" \
    "What would you like to take for profit?")
    factoryChoice = input("(Machine/Rabbit/Cheese) ")

    if factoryChoice.upper() == "MACHINE":
        print("You find a machine that is creating cheese from nothing but moon dust. This technology could be worth millions, so you tear it off its bolts and fly it out." \
        "You're chased out by flying rabbit drones firing carrot missles. Your impressive flying skills allow you to escape the the drones and get ehe technology to your fellow pirtes." \
        "You sell it on the black market for $3 million and six tickets to the Spongebob Squarepants Movie.")
        print("")
        print("THE END")
    elif factoryChoice.upper() == "RABBIT":
        print("These rabbits don't seem to be normal. They have thumbs and undertand chinese. There are so many, you don't think anyone will notice one missing." \
        "They wouldn't have, but you were greedy and took 27. You get pulled over passing Mars and the space police search your vehicle and find the rabbits." \
        "They also find many different substances that you were going to sell. You are sentenced to 16 million years of public service at the Jurassic Space Zoo, as an exibit.")
        print("")
        print("THE END")
    elif factoryChoice.upper() == "CHEESE":
        print("You actually decide that you do want the cheese, I guess, and stat taking the cheese. The cheese is fairly light, so you collect a massive stack very quickly." \
        "This does not go unnotices, many security rabbits stop you in as you feast on some swiss. You are detained and forced to work to pay for the lost profits." \
        "You work poking hole into swiss cheese for two months, and when you finally get out, you realize your spaceship was towed and you'll have to fly home.")
        print("")
        print("THE END")
    else:
        print("As you look at all the possible goodies you could take, a giant rabbit picks you up. It does not say it a word, it only thows you back up the hole." \
        "You fly into space as start thinking that maybe robbing isn't the best career option. Of course, this is a stupid thought, so you go to rob the nearest space station.")
        print("")
        print("THE END")
def hole_explode():
    print("You set up a shipload of edxplosives to blow up the hole. You don't really know why, but you think something good may happen." \
    "As you light the fuse, you start to think you may be too close. You were right. You are blown away and you notice something coming out of the blast." \
    "A giant worm almost as large as the moon itself emerges. You are kind of resposible, so you think of how to destroy it." \
    "How should you fix this problem?")
    wormChoice = input("(Fireball/Explosion/Claws)")

    if wormChoice.upper() == "FIREBALL":
        print("You begin launching fireballs at the worm. It's skin deflects the fire, but the inside of its mouth seems to be less resistant." \
        "You aim for the mouth and do some pretty good damage, but it eventually begins to cover his mouth. Seeing this you know you have to do something drastic to win." \
        "You fly into its mouth as you fire volleys of fireballs. As it closes it's mouth around you, all you could see was your fire until the mouth re opened." \
        "The worm was defeated, and you got your prize of worm teeth to sell on the black market.")
        print("")
        print("THE END")
    elif wormChoice.upper() == "EXPLOSION":
        print("You somehow have more explosive, so you begin planting them across the worm's body. You dodge all the attacks thrown by the worm until you" \
        "cover it with double the explosives used to blow the hole up. You light the fuse, this time a bit further away, and watch the worm explode." \
        "Sadly, this does nothing to the worm, it was clearly blast proof. What was not blast proof was the moon, it was completely gone. You leave defeated, but you did take" \
        "part of the moon as a participation trophy.")
        print("")
        print("THE END")
    elif wormChoice.upper() == "CLAWS":
        print("You launch towards the worm and start slashing its skin with your sharp claws. The outer layer cuts like butter, but there is just took much" \
        "and a thicker layer lies below the first. You go at it for a couple of hours, but nothing really happened. The worm was just took big, so eventually you just give up" \
        "and go to Arby's in defeat.")
        print("")
        print("THE END")
    else:
        print("You prepare to launch your attack, but the worm is surprisingly fast. It lauches at you, grabbing you and throwing you further into space." \
        "Thankfully, it cannot move through space quickly, but neither can you, so you slowly float away from it in hopes that you eventually get away.")
        print("")
        print("THE END")


def the_underworld():
    print("You find yourself in the underworld. Don't worry, you didn't do anything wrong, the gods have sent you down to slay a powerful beast" \
    "You know not where it currently resides, so you must choose a path. You can go into the brimstone mines, the forest of eternal agony," \
    "or the waffle house")
    directionChoice = input ("(Mines/Forest/Waffle) ")

    if directionChoice.upper() == "MINES":
        brimstone_mines()
    elif directionChoice.upper() == "FOREST":
        agony_forest()
    elif directionChoice.upper() == "WAFFLE":
        print("You desided to go to Waffle House. The employees, suprisingly, are not demons, they are just regular people. They get paid well and even have paid time off." \
        "You order some waffles and enoy them. They were very good, but suddenly, your cookie phone went off. It was the gods, they are not happy." \
        "They fire you on the spot, leaving you stranded in the underworld. With no other options, you get a job at Waffle House, where you work for the rest of your life.")
        print("")
        print("THE END")
    else:
        print("As you were deciding where to go, a pack of imps picked you up and dropped you into the brimstone mines")
        print("")
        brimstone_mines()

def brimstone_mines():
    print("The brimstone mines are filled with imps mining, but none are making any progress. They mine only to mine, not to gain." \
    "You see Gergabel, a demon of punishment and torture. They are one of your targets, so you must take them down. You look at your cookie jar to see what you have." \
    "There are cookies, obviously, a bottle of holy water, and a Minecraft pickaxe. What do you choose?")

    brimstoneChoice = input("(Cookie/Holy Water/Pickaxe)")

    if brimstoneChoice.upper() == "COOKIE":
        pass
    elif brimstoneChoice.upper == "HOLY WATER":
        pass
    elif brimstoneChoice.upper() == "PICKAXE":
        pass
    else:
        pass
def agony_forest():
    print("You enter the forest of eternal agony. It is filled with souls of the dead, wandering forever a they are tortured by their past." \
    "The mood is agonizing, but you know you must continue.")

    agonyChoice = input("()")

    if agonyChoice.upper() == "":
        pass
    elif agonyChoice.upper() == "":
        pass
    elif agonyChoice.upper() == "":
        pass
    else:
        pass


print("Welcome to Ben's super cool text story Game!")

print("You may be one of these three heros. " \
"Bebop, a scrap golem who specilizes in close combat with explosive punches and bombs." \
"Ridley, a space pirate dragon who ravages their enemies with molten fire breath and a sqewering tail." \
"Cookie Monster, a blue monster who loves cookies.")

playerCharacter = input("(Bebop/Ridley/Cookie Monster) ")
print("")

if playerCharacter.upper() == "RIDELY":
    ridely_picked()
elif playerCharacter.upper() == "BEBOP":
    bebop_picked()
elif playerCharacter.upper() == "COOKIE MONSTER":
    cookie_monster_picked()


