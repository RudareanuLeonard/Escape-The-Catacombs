from imports.import_libraries import *
from imports.import_files import *

# #IF I DON'T IMPORT DIRECTLY like this, the program DOES NOT WORK
# from characters.characters import *

#still need to work on those HP, AD, AS values
HP = 100
ATTACK_DAMAGE = 3
ATTACK_SPEED = 1

SUPERPOWER_DAMAGE = 30
SUPERPOWER_COOLDOWN = 40

NINJA_PATH = "characters/character_ninja/jpgs/1x/idle_0.png"

NINJA_IMAGE_SIZE = (200, 200)

class Ninja():
    def __init__(self, hp=HP, attack_damage=ATTACK_DAMAGE, attack_speed=ATTACK_SPEED,superpower_damage=SUPERPOWER_DAMAGE, superpower_cooldown=SUPERPOWER_COOLDOWN, jpg_path=NINJA_PATH, image_size=NINJA_IMAGE_SIZE):
        self.hp = hp
        self.attack_damage = attack_damage
        self.attack_speed = attack_speed
        self.superpower_damage = superpower_damage
        self.superpower_cooldown = superpower_cooldown
        self.jpg_path = jpg_path
        self.image_size = image_size
