# run this

import weapons
import classes

class Unit():
    name = ""
    classname = ""
    level = 0
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
        level = 0
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
    counter = False

    def __init__(self):
        hits = 0
        hp = 0
        damage = 0
        hit = 0
        crit = 0
        counter = False

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
            elif line[0] == "Level":
                unit.level = int(line[1])
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
    
    return 0
    
    
def geteff(attacker, defender):
    weapon1 = weapons.weapons[attacker.weapon]

    for x in weapons.removeeffect:
        if attacker.weapon == x:
            return 1

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
    for x in classes.dragon:
        if defender.classname == x:
            if weapon1.tri == "thunder":
                return 3
            for n in weapons.dragon:
                if attacker.weapon == n:
                    return 3
    for x in classes.flying:
        if defender.classname == x:
            if weapon1.tri == "wind" or weapon1.tri == "bow" or weapon.tri == "crossbow" or weapon.tri == "ballista":
                return 3
            for n in weapons.flying:
                if attacker.weapon == n:
                    return 3
    for x in classes.beast:
        if defender.classname == x:
            if weapon1.tri == "fire":
                return 3
            for n in weapons.beast:
                if attacker.weapon == n:
                    return 3
    return 1
    

def getdamage(unit1, unit2):
    unit1wpn = weapons.weapons[unit1.weapon]
    unit2wpn = weapons.weapons[unit2.weapon]

    strength = unit1.strength
    magic = unit1.magic

    if unit1wpn.tri == "crossbow" or unit1wpn.tri == "ballista":
        strength = 0
        magic = 0

    total = 0
    if unit1wpn.magic == False:
        damage = strength + ((unit1wpn.mt + gettribonus(unit1wpn, unit2wpn)) * geteff(unit1, unit2))
        total = (damage - unit2.defense)
    else:
        damage = magic + ((unit1wpn.mt + gettribonus(unit1wpn, unit2wpn)) * geteff(unit1, unit2))
        total = (damage - unit2.resistance)
    return total


def getrangebonus(weapon, rng):
    if (rng > 2 and weapon.tri == "bow") or (rng < 2 and weapon.tri == "bow"):
        return -30
    return 0

def getaccuracy(unit1, unit2, rng):
    unit1wpn = weapons.weapons[unit1.weapon]
    unit2wpn = weapons.weapons[unit2.weapon]

    total = unit1wpn.hit + (unit1.skill * 2) + unit1.luck + ((gettribonus(unit1wpn, unit2wpn) * 10) + getrangebonus(unit1wpn, rng))
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


def hitstring(hits):
    if hits > 1:
        return " x" + str(hits)
    return ""


def printrounds(unit1, unit2, round1, round2):
    print("\n")
    print(unit1.name + " with " + unit1.weapon)
    if round2.counter:
        print("HP: " + str(unit1.hp) + " -> " + str(round1.hp) + " / " + str(unit1.maxhp))
    else:
        print("HP: " + str(unit1.hp) + " / " + str(unit1.maxhp))
    print("Dmg: " + str(round1.damage) + hitstring(round1.hits))
    print("Hit: " + str(round1.hit))
    print("Crit: " + str(round1.crit))
    print("\n")
    if round2.counter:
        print(unit2.name + " with " + unit2.weapon)
        print("HP: " + str(unit2.hp) + " -> " + str(round2.hp) + " / " + str(unit2.maxhp))
        print("Dmg: " + str(round2.damage) + hitstring(round2.hits))
        print("Hit: " + str(round2.hit))
        print("Crit: " + str(round2.crit))
    else:
        print(unit2.name + " with " + unit2.weapon)
        print("HP: " + str(unit2.hp) + " -> " + str(round2.hp) + " / " + str(unit2.maxhp))
        print("Dmg: -")
        print("Hit: -")
        print("Crit: -")


def checkcombat(unit1, unit2, rng):
    unit1round = Round()
    unit2round = Round()

    unit1wpn = weapons.weapons[unit1.weapon]
    unit2wpn = weapons.weapons[unit2.weapon]

    validrng = False
    for r in unit1wpn.rng:
        if r == rng:
            validrng = True
    if validrng == False:
        print("Attacking at invalid range.")
        return 0

    for r in unit2wpn.rng:
        if r == rng:
            unit2round.counter = True

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
    unit1round.hit = max(min(getaccuracy(unit1, unit2, rng) - getavoid(unit1, unit2), 100), 0)
    unit2round.hit = max(min(getaccuracy(unit2, unit1, rng) - getavoid(unit2, unit1), 100), 0)

    #check crit
    unit1round.crit = int(max(min((unit1wpn.crt + (unit1.skill / 2) + getcritbonus(unit1)) - (unit2.luck), 100), 0))
    unit2round.crit = int(max(min((unit2wpn.crt + (unit2.skill / 2) + getcritbonus(unit2)) - (unit1.luck), 100), 0))

    #update hp
    unit1round.hp = max(unit1.hp - (unit2round.damage * unit2round.hits), 0)
    unit2round.hp = max(unit2.hp - (unit1round.damage * unit1round.hits), 0)

    #print
    printrounds(unit1, unit2, unit1round, unit2round)

    return 0


def printheal(unit1, unit2):
    healed = unit1.magic + weapons.staffheal[unit1.weapon]

    print("\n")
    print(unit1.name + " with " + unit1.weapon)
    print(unit2.name + " HP: "+ str(unit2.hp) + " -> " + str(min(unit2.hp + healed, unit2.maxhp)) + " / " + str(unit2.maxhp))


    
def staffcombat(unit1, unit2, rng):
    unit1round = Round()
    unit2round = Round()

    unit1wpn = weapons.weapons[unit1.weapon]
    unit2wpn = weapons.weapons[unit2.weapon]

    heal = True

    for n in weapons.offensestaves:
        if unit1.weapon == n:
            heal = False

    if heal:
        printheal(unit1, unit2)
        
    else:

        unit1round.hit = (30 + ((unit1.magic - unit2.resistance) * 5) + unit1.skill) - (rng * 2)
        unit2round.hp = unit2.hp

        for r in unit2wpn.rng:
            if r == rng:
                unit2round.counter = True

        if unit2round.counter:
            attacksp1 = unit1.speed - max(unit1wpn.wt - unit1.strength, 0)
            attacksp2 = unit2.speed - max(unit2wpn.wt - unit2.strength, 0)

            if (attacksp2 - attacksp1 >= 4):
                unit2round.hits = 2
            else:
                unit2round.hits = 1

            unit2round.damage = getdamage(unit2, unit1)
            unit2round.hit = max(min(getaccuracy(unit2, unit1, rng) - getavoid(unit2, unit1), 100), 0)
            unit2round.crit = int(max(min((unit2wpn.crt + (unit2.skill / 2) + getcritbonus(unit2)) - (unit1.luck), 100), 0))
            unit1round.hp = max(unit1.hp - (unit2round.damage * unit2round.hits), 0)


        printrounds(unit1, unit2, unit1round, unit2round)

def checkstaffrange(unit1, rng):
    for n in weapons.rangedmag:
        if (n == unit1.weapon):
            if (rng <= (unit1.magic // 2)):
                return True
            else:
                return False
    for n in weapons.rangedset:
        if (n == unit1.weapon):
            if (rng <= 30):
                return True
            else:
                return False
    return True

def main():

    cont = True

    while cont:

        print("\n")
        unit1name = input("Attacking: ")
        unit2name = input("Defending: ")
        rng = int(input("At range: "))

        unit1 = readunit(unit1name + ".txt")
        unit2 = readunit(unit2name + ".txt")

        if weapons.weapons[unit1.weapon].tri == "staff":
            if checkstaffrange(unit1, rng):
                staffcombat(unit1, unit2, rng)
            else:
                print("Attacking from invalid range.")
        else:
            checkcombat(unit1, unit2, int(rng))

        print("\n")
        ex = input("Enter n to end or press any other key to continue: ")
        if ex == "n":
            cont = False
            print("\n")


    


if __name__ == "__main__":
    main()

