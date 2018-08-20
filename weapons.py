#weapon library for stat lookup

class Weapon():
    wt = 0
    mt = 0
    hit = 0
    crt = 0
    magic = False
    tri = ""

    def __init__(self, wtin, mtin, hitin, crtin, mag, tri):
        self.wt = wtin
        self.mt = mtin
        self.hit = hitin
        self.crt = crtin
        self.magic = mag
        self.tri = tri


#weapons by effect
brave = ["Brave Sword", "Brave Axe", "Brave Lance", "Brave Bow", "Amiti"]
armor = ["Hammer", "Thani"]
cavalry = ["Horseslayer", "Thani"]

weapons = {
    "Slim Sword": Weapon(3, 2, 100, 5, False, "sword"),
    "Bronze Sword": Weapon(5, 3, 95, 0, False, "sword"),
    "Iron Sword": Weapon(7, 6, 90, 0, False, "sword"),
    "Venin Edge": Weapon(7, 6, 90, 0, False, "sword"),
    "Wind Edge": Weapon(10, 6, 60, 0, False, "sword"),
    "Steel Sword": Weapon(11, 9, 85, 0, False, "sword"),
    "Brave Sword": Weapon(9, 9, 90, 0, False, "sword"),
    "Iron Blade": Weapon(13, 10, 70, 0, False, "sword"),
    "Wo Dao": Weapon(7, 7, 90, 20, False, "sword"),
    "Killing Edge": Weapon(8, 8, 85, 30, False, "sword"),
    "Wyrmslayer": Weapon(14, 11, 70, 0, False, "sword"),
    "Steel Blade": Weapon(17, 13, 65, 0, False, "sword"),
    "Storm Sword": Weapon(11, 12, 50, 0, False, "sword"),
    "Silver Sword": Weapon(10, 12, 80, 0, False, "sword"),
    "Silver Blade": Weapon(16, 16, 60, 0, False, "sword"),
    "Tempest Blade": Weapon(15, 18, 55, 5, False, "sword"),
    "Vague Katti": Weapon(10, 20, 95, 5, False, "sword"),
    "Alondite": Weapon(20, 18, 80, 5, False, "sword"),
    "Ettard": Weapon(15, 14, 95, 5, False, "sword"),
    "Florete": Weapon(15, 14, 95, 15, True, "sword"),
    "Caladbolg": Weapon(8, 15, 85, 5, False, "sword"),
    "Amiti": Weapon(10, 15, 90, 0, False, "sword"),
    "Ragnell": Weapon(20, 18, 80, 5, False, "sword"),
    "Iron Axe": Weapon(11, 8, 80, 0, False, "axe")
}