# run this

import weapons
import classes

class Unit():
    name = ""
    classname = ""
    hp = 0
    maxhp = 0
    strength = 0
    magic = 0
    skill = 0
    speed = 0
    luck = 0
    defense = 0
    resistance = 0
    weapon = ""

    def __init__(self):
        name = ""
        classname = ""
        hp = 0
        maxhp = 0
        strength = 0
        magic = 0
        skill = 0
        speed = 0
        luck = 0
        defense = 0
        resistance = 0
        weapon = ""

class Round():
    hits = 0
    hp = 0
    damage = 0
    hit = 0
    crit = 0

    def __init__(self):
        hits = 0
        hp = 0
        damage = 0
        hit = 0
        crit = 0

def readunit(name):
    fd = open(name, "r")

    unit = Unit()

    for l in fd:
        if len(l) >= 2:
            line = l.split()
            if line[0] == "Name":
                unit.name = wordgather(line)
            elif line[0] == "Class":
                unit.classname = wordgather(line)
            elif line[0] == "HP":
                unit.hp = int(line[1])
            elif line[0] == "Max":
                unit.maxhp = int(line[1])
            elif line[0] == "Str":
                unit.strength = int(line[1])
            elif line[0] == "Mag":
                unit.magic = int(line[1])
            elif line[0] == "Skill":
                unit.skill = int(line[1])
            elif line[0] == "Sp":
                unit.speed = int(line[1])
            elif line[0] == "Luck":
                unit.luck = int(line[1])
            elif line[0] == "Def":
                unit.defense = int(line[1])
            elif line[0] == "Res":
                unit.resistance = int(line[1])
            elif line[0] == "Weapon":
                unit.weapon = wordgather(line)
        else:
            print("Improper stat format.")

    fd.close()
    return unit

def wordgather(line):
    w = ""
    for x in range(1, len(line)):
        w = w + line[x] + " "
    return w.strip(" ")

def checkattr(attr, unit, round):
    for n in attr:
        if unit.weapon == n:
            round.hits = round.hits * 2

def gettribonus(wpn1, wpn2):
    if wpn1.tri == "sword":
        if wpn2.tri == "axe":
            return 1
        elif wpn2.tri == "lance":
            return -1
    elif wpn1.tri == "axe":
        if wpn2.tri == "lance":
            return 1
        elif wpn2.tri == "sword":
            return -1
    elif wpn1.tri == "lance":
        if wpn2.tri == "sword":
            return 1
        elif wpn2.tri == "axe":
            return -1
    elif wpn1.tri == "fire":
        if wpn2.tri == "wind" or wpn2.tri == "light":
            return 1
        elif wpn2.tri == "thunder" or wpn2.tri == "dark":
            return -1
    elif wpn1.tri == "wind":
        if wpn2.tri == "thunder" or wpn2.tri == "light":
            return 1
        elif wpn2.tri == "fire" or wpn2.tri == "dark":
            return -1
    elif wpn1.tri == "thunder":
        if wpn2.tri == "fire" or wpn2.tri == "light":
            return 1
        elif wpn2.tri == "wind" or wpn2.tri == "dark":
            return -1
    elif wpn1.tri == "dark":
        if wpn2.tri == "fire" or wpn2.tri == "thunder" or wpn2.tri == "wind":
            return 1
        elif wpn2.tri == "light":
            return -1
    elif wpn1.tri == "light":
        if wpn2.tri == "dark":
            return 1
        elif wpn2.tri == "fire" or wpn2.tri == "thunder" or wpn2.tri == "wind":
            return -1
    else:
        return 0
    
    
def geteff(attacker, defender):
    for x in classes.armor:
        if defender.classname == x:
            for n in weapons.armor:
                if attacker.weapon == n:
                    return 3
    for x in classes.cavalry:
        if defender.classname == x:
            for n in weapons.cavalry:
                if attacker.weapon == n:
                    return 3
    return 1
    

def getdamage(unit1, unit2):
    unit1wpn = weapons.weapons[unit1.weapon]
    unit2wpn = weapons.weapons[unit2.weapon]

    total = 0
    if unit1wpn.magic == False:
        damage = unit1.strength + (unit1wpn.mt + gettribonus(unit1wpn, unit2wpn) * geteff(unit1wpn, unit2))
        total = (damage - unit2.defense)
    else:
        damage = unit1.magic + (unit1wpn.mt + gettribonus(unit1wpn, unit2wpn) * geteff(unit1, unit2))
        total = (damage - unit2.resistance)
    return total


def getaccuracy(unit1, unit2):
    unit1wpn = weapons.weapons[unit1.weapon]
    unit2wpn = weapons.weapons[unit2.weapon]

    total = unit1wpn.hit + (unit1.skill * 2) + unit1.luck + (gettribonus(unit1wpn, unit2wpn) * 10)
    return total


def getavoid(unit1, unit2):
    unit1wpn = weapons.weapons[unit1.weapon]
    unit2wpn = weapons.weapons[unit2.weapon]

    total = ((unit1.speed - max(unit1wpn.wt - unit1.strength, 0)) * 2) + unit1.luck
    return total


def getcritbonus(unit):
    for n in classes.crit5:
        if unit.classname == n:
            return 5
    for n in classes.crit10:
        if unit.classname == n:
            return 10
    for n in classes.crit15:
        if unit.classname == n:
            return 15
    for n in classes.crit20:
        if unit.classname == n:
            return 20
    for n in classes.crit25:
        if unit.classname == n:
            return 25
    return 0



def printrounds(unit1, unit2, round1, round2):
    print("\n")
    print(unit1.name)
    print("HP: " + str(unit1.hp) + " -> " + str(round1.hp) + " / " + str(unit1.maxhp))
    print("Dmg: " + str(round1.damage) + " x" + str(round1.hits))
    print("Hit: " + str(round1.hit))
    print("Crit: " + str(round1.crit))
    print("\n")
    print(unit2.name)
    print("HP: " + str(unit2.hp) + " -> " + str(round2.hp) + " / " + str(unit2.maxhp))
    print("Dmg: " + str(round2.damage) + " x" + str(round2.hits))
    print("Hit: " + str(round2.hit))
    print("Crit: " + str(round2.crit))


def checkcombat(unit1, unit2):
    unit1round = Round()
    unit2round = Round()

    unit1wpn = weapons.weapons[unit1.weapon]
    unit2wpn = weapons.weapons[unit2.weapon]

    #check speed
    attacksp1 = unit1.speed - max(unit1wpn.wt - unit1.strength, 0)
    attacksp2 = unit2.speed - max(unit2wpn.wt - unit2.strength, 0)

    if (attacksp1 - attacksp2 >= 4):
        unit1round.hits = 2
    else:
        unit1round.hits = 1

    if (attacksp2 - attacksp1 >= 4):
        unit2round.hits = 2
    else:
        unit2round.hits = 1

    checkattr(weapons.brave, unit1, unit1round)
    checkattr(weapons.brave, unit2, unit2round)


    #check damage
    unit1round.damage = getdamage(unit1, unit2)
    unit2round.damage = getdamage(unit2, unit1)

    #check hit
    unit1round.hit = max(min(getaccuracy(unit1, unit2) - getavoid(unit1, unit2), 100), 0)
    unit2round.hit = max(min(getaccuracy(unit2, unit1) - getavoid(unit2, unit1), 100), 0)

    #check crit
    unit1round.crit = int(max(min((unit1wpn.crt + (unit1.skill / 2) + getcritbonus(unit1)) - (unit2.luck), 100), 0))
    unit2round.crit = int(max(min((unit2wpn.crt + (unit2.skill / 2) + getcritbonus(unit2)) - (unit1.luck), 100), 0))

    #update hp
    unit1round.hp = max(unit1.hp - (unit2round.damage * unit2round.hits), 0)
    unit2round.hp = max(unit2.hp - (unit1round.damage * unit1round.hits), 0)

    #print
    printrounds(unit1, unit2, unit1round, unit2round)




def main():
    unit1name = input("Unit 1: ")
    unit2name = input("Unit 2: ")

    unit1 = readunit(unit1name + ".txt")
    unit2 = readunit(unit2name + ".txt")

    checkcombat(unit1, unit2)


    


if __name__ == "__main__":
    main()

