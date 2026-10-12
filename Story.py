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
    elif powerChoice.upper() == "Hunt":
        print("thing")
    else:
        print("As you were about to go forward with your plan, the Allmother demands that you defend the gurdian, so you do.")
        print("")
        defend_gurdian()

def defend_gurdian():
    pass
def farm_creeps():
    pass

def the_Moon():
    print("You find yourself on the moon, a barren wasteland at first glance, but you know there is bountiful treasure somewhere." \
    "You stumble upon a deep hole, so deep you can't see the bottom. You have brought lots of equiptment, a pirate is always prepared." \
    "What would you like to do?")
    holeChoice = input("(jump/Explode/Fill) ")

    if holeChoice.upper() == "JUMP":
        hole_jump()
    elif holeChoice.upper() == "EXPLODE":
        hole_explode
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
    pass
def hole_explode():
    pass

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
    pass
def agony_forest():
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


