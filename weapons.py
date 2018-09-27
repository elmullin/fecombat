#weapon library for stat lookup

class Weapon():
    wt = 0
    mt = 0
    hit = 0
    crt = 0
    magic = False
    tri = ""
    rng = []

    def __init__(self, wtin, mtin, hitin, crtin, mag, tri, rng):
        self.wt = wtin
        self.mt = mtin
        self.hit = hitin
        self.crt = crtin
        self.magic = mag
        self.tri = tri
        self.rng = rng


#weapons by effect - add weapons to these lists to give them effects
#not required for bows/wind vs flying, thunder vs dragons, or fire vs beasts
#those use the weapon's type ("tri" value)
#hpdrain not implemented

brave = ["Brave Sword", "Brave Axe", "Brave Lance", "Brave Bow", "Amiti"]
armor = ["Hammer", "Thani"]
cavalry = ["Horseslayer", "Thani"]
flying = []
beast = ["Beast Killer"]
dragon = ["Wyrmslayer"]
hpdrain = ["Nosferatu"]
removeeffect = ["Wind Tail", "Fire Tail", "Thunder Tail", "Onager"]
nocrit = ["Wind Tail", "Fire Tail", "Thunder Tail", "Bronze Knife", "Bronze Dagger", "Onager", "Bronze Bow", "Bronze Axe", "Bronze Lance", "Bronze Sword"]

#staff stuff

offensestaves = ["Sleep", "Elsleep", "Silence", "Elsilence"]
healstaves = ["Heal", "Mend", "Physic", "Recover", "Fortify", "Matrona", "Ashera Staff"]
rangedmag = ["Physic," "Fortify", "Matrona", "Silence", "Sleep"]
rangedset = ["Elsilence", "Elsleep"]

#hit and heal values for staves when initiating action

staffhit = {
    "Sleep": 65,
    "Silence": 70,
    "Elsilence": 80,
    "Elsleep": 75
}

staffheal = {
    "Heal": 10,
    "Mend": 20,
    "Physic": 10,
    "Recover": 100,
    "Fortify": 10,
    "Matrona": 100,
    "Ashera Staff": 100
}


#to add a new weapon
#"<Weapon Name>": Weapon(<Wt>, <Mt>, <Hit>, <Crit>, <Magic damage? True/False>, <Type>, <Array of valid ranges>)
#requires commas between entries!

weapons = {
    "None": Weapon(0, 0, 0, 0, False, "none", []),
    "None (Laguz)": Weapon(0, 0, 80, 0, False, "none", [1]),
    "Slim Sword": Weapon(3, 2, 100, 5, False, "sword", [1]),
    "Bronze Sword": Weapon(5, 3, 95, 0, False, "sword", [1]),
    "Iron Sword": Weapon(7, 6, 90, 0, False, "sword", [1]),
    "Venin Edge": Weapon(7, 6, 90, 0, False, "sword", [1]),
    "Wind Edge": Weapon(10, 6, 60, 0, False, "sword", [1, 2]),
    "Steel Sword": Weapon(11, 9, 85, 0, False, "sword", [1]),
    "Brave Sword": Weapon(9, 9, 90, 0, False, "sword", [1]),
    "Iron Blade": Weapon(13, 10, 70, 0, False, "sword", [1]),
    "Wo Dao": Weapon(7, 7, 90, 20, False, "sword", [1]),
    "Killing Edge": Weapon(8, 8, 85, 30, False, "sword", [1]),
    "Wyrmslayer": Weapon(14, 11, 70, 0, False, "sword", [1]),
    "Steel Blade": Weapon(17, 13, 65, 0, False, "sword", [1]),
    "Storm Sword": Weapon(11, 12, 50, 0, False, "sword", [1, 2]),
    "Silver Sword": Weapon(10, 12, 80, 0, False, "sword", [1]),
    "Silver Blade": Weapon(16, 16, 60, 0, False, "sword", [1]),
    "Tempest Blade": Weapon(15, 18, 55, 5, False, "sword", [1, 2]),
    "Vague Katti": Weapon(10, 20, 95, 5, False, "sword", [1]),
    "Alondite": Weapon(20, 18, 80, 5, False, "sword", [1, 2]),
    "Ettard": Weapon(15, 14, 95, 5, False, "sword", [1]),
    "Florete": Weapon(15, 14, 95, 15, True, "sword", [1, 2]),
    "Caladbolg": Weapon(8, 15, 85, 5, False, "sword", [1]),
    "Amiti": Weapon(10, 15, 90, 0, False, "sword", [1]),
    "Ragnell": Weapon(20, 18, 80, 5, False, "sword", [1, 2]),
    "Slim Lance": Weapon(4, 3, 95, 5, False, "lance", [1]),
    "Bronze Lance": Weapon(6, 4, 90, 0, False, "lance", [1]),
    "Iron Lance": Weapon(9, 7, 85, 0, False, "lance", [1]),
    "Venin Lance": Weapon(9, 7, 85, 0, False, "lance", [1]),
    "Javelin": Weapon(11, 7, 65, 0, False, "lance", [1, 2]),
    "Horseslayer": Weapon(15, 12, 65, 0, False, "lance", [1]),
    "Steel Lance": Weapon(13, 10, 80, 0, False, "lance", [1]),
    "Brave Lance": Weapon(11, 10, 85, 0, False, "lance", [1]),
    "Iron Greatlance": Weapon(14, 11, 75, 0, False, "lance", [1]),
    "Killer Lance": Weapon(10, 9, 80, 30, False, "lance", [1]),
    "Short Spear": Weapon(12, 10, 55, 0, False, "lance", [1, 2]),
    "Steel Greatlance": Weapon(18, 14, 70, 0, False, "lance", [1]),
    "Silver Lance": Weapon(12, 13, 80, 0, False, "lance", [1]),
    "Silver Greatlance": Weapon(17, 17, 50, 0, False, "lance", [1]),
    "Spear": Weapon(16, 13, 60, 5, False, "lance", [1, 2]),
    "Wishblade": Weapon(15, 22, 100, 5, False, "lance", [1, 2]),
    "Bronze Axe": Weapon(7, 5, 85, 0, False, "axe", [1]),
    "Iron Axe": Weapon(11, 8, 80, 0, False, "axe", [1]),
    "Venin Axe": Weapon(11, 8, 80, 0, False, "axe", [1]),
    "Hand Axe": Weapon(12, 9, 75, 0, False, "axe", [1, 2]),
    "Hammer": Weapon(17, 13, 60, 0, False, "axe", [1]),
    "Steel Axe": Weapon(15, 11, 75, 0, False, "axe", [1]),
    "Brave Axe": Weapon(13, 11, 80, 0, False, "axe", [1]),
    "Iron Poleax": Weapon(16, 12, 65, 0, False, "axe", [1]),
    "Killer Axe": Weapon(12, 10, 75, 30, False, "axe", [1]),
    "Short Axe": Weapon(13, 12, 60, 0, False, "axe", [1, 2]),
    "Steel Poleax": Weapon(20, 15, 60, 0, False, "axe", [1]),
    "Silver Axe": Weapon(14, 14, 70, 0, False, "axe", [1]),
    "Silver Poleax": Weapon(19, 18, 60, 0, False, "axe", [1]),
    "Tomahawk": Weapon(17, 15, 65, 5, False, "axe", [1, 2]),
    "Urvan": Weapon(17, 22, 110, 5, False, "axe", [1]),
    "Tarvos": Weapon(12, 18, 100, 5, False, "axe", [1]),
    "Bronze Bow": Weapon(4, 3, 80, 0, False, "bow", [2]),
    "Iron Bow": Weapon(8, 6, 85, 0, False, "bow", [2]),
    "Venin Bow": Weapon(8, 6, 85, 0, False, "bow", [2]),
    "Killer Bow": Weapon(9, 8, 80, 30, False, "bow", [2]),
    "Rolf's Bow": Weapon(8, 8, 85, 0, False, "bow", [2]),
    "Iron Longbow": Weapon(15, 8, 65, 0, False, "bow", [2, 3]),
    "Steel Bow": Weapon(10, 10, 80, 0, False, "bow", [2]),
    "Brave Bow": Weapon(10, 9, 85, 0, False, "bow", [2]),
    "Steel Longbow": Weapon(18, 12, 60, 0, False, "bow", [2, 3]),
    "Silver Bow": Weapon(9, 15, 75, 0, False, "bow", [2]),
    "Silencer": Weapon(6, 16, 100, 5, False, "bow", [2]),
    "Silver Longbow": Weapon(17, 17, 55, 0, False, "bow", [2, 3]),
    "Double Bow": Weapon(12, 22, 100, 5, False, "bow", [1, 2]),
    "Lughnasadh": Weapon(5, 16, 100, 5, False, "bow", [2]),
    "Bowgun": Weapon(12, 24, 100, 0, False, "crossbow", [1, 2]),
    "Crossbow": Weapon(14, 28, 100, 0, False, "crossbow", [1, 2]),
    "Taksh": Weapon(16, 30, 100, 10, False, "crossbow", [1, 2]),
    "Aqqar": Weapon(18, 34, 100, 0, False, "crossbow", [1, 2]),
    "Arbalest": Weapon(20, 38, 100, 15, False, "crossbow", [1, 2]),
    "Ballista": Weapon(20, 18, 100, 0, False, "ballista", [3, 4, 5, 6, 7, 8, 9, 10]),
    "Iron Ballista": Weapon(20, 28, 90, 0, False, "ballista", [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    "Killer Ballista": Weapon(20, 26, 95, 10, False, "ballista", [3, 4, 5, 6, 7, 8, 9, 10]),
    "Onager": Weapon(20, 22, 255, 0, False, "ballista", [3, 4, 5, 6, 7, 8, 9, 10]),
    "Bronze Knife": Weapon(1, 1, 70, 0, False, "knife", [1, 2]),
    "Bronze Dagger": Weapon(1, 2, 85, 0, False, "knife", [1]),
    "Iron Knife": Weapon(2, 2, 65, 0, False, "knife", [1, 2]),
    "Beast Killer": Weapon(8, 9, 65, 0, False, "knife", [1]),
    "Steel Knife": Weapon(3, 4, 60, 0, False, "knife", [1, 2]),
    "Iron Dagger": Weapon(3, 5, 80, 5, False, "knife", [1]),
    "Kard": Weapon(6, 4, 70, 10, False, "knife", [1]),
    "Steel Dagger": Weapon(5, 8, 85, 5, False, "knife", [1]),
    "Silver Knife": Weapon(4, 7, 60, 0, False, "knife", [1, 2]),
    "Stiletto": Weapon(8, 8, 80, 20, False, "knife", [1]),
    "Silver Dagger": Weapon(7, 12, 85, 5, False, "knife", [1]),
    "Peshkatz": Weapon(9, 13, 90, 0, False, "knife", [1, 2]),
    "Baselard": Weapon(10, 18, 100, 15, False, "knife", [1]),
    "Wolf Fang A": Weapon(1, 9, 90, 0, False, "strike", [1]),
    "Wolf Fang S": Weapon(1, 14, 90, 0, False, "strike", [1]),
    "Wolf Fang SS": Weapon(1, 19, 90, 0, False, "strike", [1]),
    "Wolf Great Fang A": Weapon(1, 10, 90, 0, False, "strike", [1]),
    "Wolf Great Fang S": Weapon(1, 15, 90, 0, False, "strike", [1]),
    "Wolf Great Fang SS": Weapon(1, 20, 100, 0, False, "strike", [1]),
    "Tiger Fang A": Weapon(1, 10, 90, 0, False, "strike", [1]),
    "Tiger Fang S": Weapon(1, 15, 90, 0, False, "strike", [1]),
    "Tiger Fang SS": Weapon(1, 20, 90, 0, False, "strike", [1]),
    "Lion Fang A": Weapon(1, 11, 95, 0, False, "strike", [1]),
    "Lion Fang S": Weapon(1, 16, 95, 0, False, "strike", [1]),
    "Lion Fang SS": Weapon(1, 21, 95, 0, False, "strike", [1]),
    "Lion Great Fang A": Weapon(1, 12, 95, 0, False, "strike", [1]),
    "Lion Great Fang S": Weapon(1, 17, 100, 0, False, "strike", [1]),
    "Lion Great Fang SS": Weapon(1, 22, 100, 0, False, "strike", [1]),
    "Claw A": Weapon(1, 8, 90, 0, False, "strike", [1]),
    "Claw S": Weapon(1, 13, 90, 0, False, "strike", [1]),
    "Claw SS": Weapon(1, 18, 90, 0, False, "strike", [1]),
    "Beak A": Weapon(1, 7, 90, 0, False, "strike", [1]),
    "Beak S": Weapon(1, 12, 90, 0, False, "strike", [1]),
    "Beak SS": Weapon(1, 17, 90, 0, False, "strike", [1]),
    "Great Beak A": Weapon(1, 8, 95, 0, False, "strike", [1]),
    "Great Beak S": Weapon(1, 13, 95, 0, False, "strike", [1]),
    "Great Beak SS": Weapon(1, 18, 100, 0, False, "strike", [1]),
    "Talon A": Weapon(1, 8, 90, 0, False, "strike", [1]),
    "Talon S": Weapon(1, 13, 90, 0, False, "strike", [1]),
    "Talon SS": Weapon(1, 18, 90, 0, False, "strike", [1]),
    "Great Talon A": Weapon(1, 10, 100, 0, False, "strike", [1]),
    "Great Talon S": Weapon(1, 15, 100, 0, False, "strike", [1]),
    "Great Talon SS": Weapon(1, 20, 100, 0, False, "strike", [1]),
    "Red Breath A": Weapon(1, 13, 90, 0, False, "strike", [1, 2]),
    "Red Breath S": Weapon(1, 18, 90, 0, False, "strike", [1, 2]),
    "Read Breath SS": Weapon(1, 23, 100, 0, False, "strike", [1, 2]),
    "White Breath A": Weapon(1, 11, 90, 0, True, "strike", [1, 2]),
    "White Breath S": Weapon(1, 16, 100, 0, True, "strike", [1, 2]),
    "White Breath SS": Weapon(1, 21, 110, 0, True, "strike", [1, 2]),
    "Black Breath A": Weapon(1, 12, 95, 0, False, "strike", [1, 2]),
    "Black Breath S": Weapon(1, 17, 105, 0, False, "strike", [1, 2]),
    "Black Breath SS": Weapon(1, 22, 115, 0, False, "strike", [1, 2]),
    "Great Black Breath A": Weapon(1, 15, 95, 0, False, "strike", [1, 2]),
    "Great Black Breath S": Weapon(1, 20, 105, 0, False, "strike", [1, 2]),
    "Great Black Breath SS": Weapon(1, 25, 115, 0, False, "strike", [1, 2]),
    "Fire": Weapon(3, 5, 90, 0, True, "fire", [1, 2]),
    "Elire": Weapon(5, 7, 85, 0, True, "fire", [1, 2]),
    "Meteor": Weapon(18, 8, 70, 0, True, "fire", [3, 4, 5, 6, 7, 8, 9, 10]),
    "Arcfire": Weapon(7, 9, 80, 5, True, "fire", [1, 2]),
    "Bolganone": Weapon(9, 11, 75, 0, True, "fire", [1, 2]),
    "Rexflame": Weapon(13, 14, 100, 5, True, "fire", [1, 2]),
    "Fire Tail": Weapon(1, 13, 85, 0, True, "fire", [1, 2]),
    "Cymbeline": Weapon(5, 13, 95, 10, True, "fire", [1, 2]),
    "Thunder": Weapon(4, 3, 80, 5, True, "thunder", [1, 2]),
    "Elthunder": Weapon(6, 5, 75, 10, True, "thunder", [1, 2]),
    "Bolting": Weapon(19, 6, 60, 5, True, "thunder", [3, 4, 5, 6, 7, 8, 9, 10]),
    "Arcthunder": Weapon(9, 7, 90, 15, True, "thunder", [1, 2]),
    "Thoron": Weapon(11, 9, 65, 5, True, "thunder", [1, 2]),
    "Rexbolt": Weapon(14, 12, 95, 15, True, "thunder", [1, 2]),
    "Thunder Tail": Weapon(1, 11, 75, 0, True, "thunder", [1, 2]),
    "Wind": Weapon(2, 4, 95, 0, True, "wind", [1, 2]),
    "Elwind": Weapon(4, 6, 90, 0, True, "wind", [1, 2]),
    "Blizzard": Weapon(17, 7, 75, 0, True, "wind", [3, 4, 5, 6, 7, 8, 9, 10]),
    "Arcwind": Weapon(6, 8, 85, 10, True, "wind", [1, 2]),
    "Tornado": Weapon(7, 10, 80, 0, True, "wind", [1, 2]),
    "Rexcalibur": Weapon(12, 13, 105, 10, True, "wind", [1, 2]),
    "Wind Tail": Weapon(1, 12, 90, 0, True, "wind", [1, 2]),
    "Light": Weapon(1, 3, 100, 0, True, "light", [1, 2]),
    "Ellight": Weapon(3, 5, 95, 0, True, "light", [1, 2]),
    "Purge": Weapon(16, 5, 80, 0, True, "light", [3, 4, 5, 6, 7, 8, 9, 10]),
    "Shine": Weapon(5, 7, 90, 10, True, "light", [1, 2]),
    "Nosferatu": Weapon(7, 6, 85, 0, True, "light", [1, 2]),
    "Valarua": Weapon(12, 8, 95, 0, True, "light", [1, 2]),
    "Rexaura": Weapon(11, 12, 110, 5, True, "light", [1, 2]),
    "Thani": Weapon(1, 8, 100, 0, True, "light", [1, 2]),
    "Creiddylad": Weapon(15, 11, 100, 15, True, "light", [1, 2]),
    "Worm": Weapon(9, 8, 75, 0, True, "dark", [1, 2]),
    "Carreau": Weapon(11, 10, 70, 5, True, "dark", [1, 2]),
    "Fenrir": Weapon(20, 9, 60, 0, True, "dark", [3, 4, 5, 6, 7, 8, 9, 10]),
    "Verrine": Weapon(13, 12, 65, 0, True, "dark", [1, 2]),
    "Balberith": Weapon(15, 15, 75, 10, True, "dark", [1, 2]),
    "Heal": Weapon(2, 1, 100, 5, False, "staff", [1]),
    "Mend": Weapon(4, 1, 100, 10, False, "staff", [1]),
    "Torch": Weapon(7, 1, 100, 15, False, "staff", [1]),
    "Unlock": Weapon(7, 1, 100, 15, False, "staff", [1]),
    "Restore": Weapon(4, 1, 100, 15, False, "staff", [1]),
    "Ward": Weapon(4, 1, 100, 20, False, "staff", [1]),
    "Physic": Weapon(5, 1, 100, 25, False, "staff", [1]),
    "Hammerne": Weapon(7, 1, 100, 25, False, "staff", [1]),
    "Recover": Weapon(6, 1, 100, 20, False, "staff", [1]),
    "Sleep": Weapon(6, 1, 100, 35, False, "staff", [1]),
    "Rescue": Weapon(6, 1, 100, 40, False, "staff", [1]),
    "Silence": Weapon(7, 1, 100, 30, False, "staff", [1]),
    "Rewarp": Weapon(7, 1, 100, 30, False, "staff", [1]),
    "Elsilence": Weapon(7, 1, 100, 30, False, "staff", [1]),
    "Elsleep": Weapon(8, 1, 100, 35, False, "staff", [1]),
    "Fortify": Weapon(7, 1, 100, 50, False, "staff", [1]),
    "Matrona": Weapon(3, 1, 100, 100, False, "staff", [1]),
    "Ashera Staff": Weapon(4, 1, 100, 100, False, "staff", [1]),
    "Judge": Weapon(16, 50, 100, 0, False, "judge", [1, 2])
}