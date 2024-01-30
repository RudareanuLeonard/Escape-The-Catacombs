from imports.import_files import *
from imports.import_libraries import *

#IF I DON'T IMPORT DIRECTLY like this, the program DOES NOT WORK
# from characters.characters import *

#still need to work on those HP, AD, AS values
HP = 90
ATTACK_DAMAGE = 4
ATTACK_SPEED = 2

SUPERPOWER_DAMAGE = 40
SUPERPOWER_COOLDOWN = 45

PIRATE_IMAGE_SIZE = (200, 200)

PIRATE_PATH = "characters/character_pirate/jpgs/1x/idle_0.png"

class Pirate():
    def __init__(self, hp=HP, attack_damage=ATTACK_DAMAGE, attack_speed=ATTACK_SPEED, superpower_damage=SUPERPOWER_DAMAGE, superpower_cooldown=SUPERPOWER_COOLDOWN, jpg_path=PIRATE_PATH, image_size = PIRATE_IMAGE_SIZE):
        self.hp = hp
        self.attack_damage = attack_damage
        self.attack_speed = attack_speed
        self.superpower_damage = superpower_damage
        self.superpower_cooldown = superpower_cooldown
        self.jpg_path = jpg_path
        self.image_size = image_size
