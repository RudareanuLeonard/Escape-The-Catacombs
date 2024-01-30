

#IF I DON'T IMPORT DIRECTLY like this, the program DOES NOT WORK


#still need to work on those HP, AD, AS values
HP = 85
ATTACK_DAMAGE = 5
ATTACK_SPEED = 3

SUPERPOWER_DAMAGE = 32
SUPERPOWER_COOLDOWN = 35

VIKING_IMAGE_SIZE = (200, 200)

VIKING_PATH = "characters/character_viking/jpgs/1x/idle_0.png"

class Viking():
    def __init__(self, hp=HP, attack_damage=ATTACK_DAMAGE, attack_speed=ATTACK_SPEED, superpower_damage=SUPERPOWER_DAMAGE, superpower_cooldown=SUPERPOWER_COOLDOWN, jpg_path=VIKING_PATH, image_size=VIKING_IMAGE_SIZE):
        self.hp = hp
        self.attack_damage = attack_damage
        self.attack_speed = attack_speed
        self.superpower_damage = superpower_damage
        self.superpower_cooldown = superpower_cooldown
        self.jpg_path = jpg_path
        self.image_size = VIKING_IMAGE_SIZE
