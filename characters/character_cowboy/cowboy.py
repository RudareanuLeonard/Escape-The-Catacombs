from imports.import_files import *
from imports.import_libraries import *

#IF I DON'T IMPORT DIRECTLY like this, the program DOES NOT WORK
# from characters.characters import *

#still need to work on those HP, AD, AS values
HP = 80
ATTACK_DAMAGE = 7
ATTACK_SPEED = 4


SUPERPOWER_DAMAGE = 20
SUPERPOWER_COOLDOWN = 25

COWBOY_IMAGE_SIZE = (200, 200)

COWBOY_PATH = "characters/character_cowboy/jpgs/Cowboy4_idle with gun_1.png"

class Cowboy():
    def __init__(self, hp=HP, attack_damage=ATTACK_DAMAGE, attack_speed=ATTACK_SPEED, superpower_damage=SUPERPOWER_DAMAGE, superpower_cooldown=SUPERPOWER_COOLDOWN, jpg_path=COWBOY_PATH, image_size=COWBOY_IMAGE_SIZE):
        self.hp = hp
        self.attack_damage = attack_damage
        self.attack_speed = attack_speed
        self.superpower_damage = superpower_damage
        self.superpower_cooldown = superpower_cooldown
        self.jpg_path = jpg_path
        self.image_size = image_size
