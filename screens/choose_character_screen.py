from imports.import_libraries import *
from imports.import_files import *

#IF I DONT IMPORT DIRECTLY, IT DOESNT WORK ------ because of inheritance
from characters.character_ninja.ninja import *
from characters.character_cowboy.cowboy import *
from characters.character_pirate.pirate import *
from characters.character_viking.viking import *


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

BG_COLOR = "red"
TEXT_COLOR = "black"

FONT_PATH = "fonts/NoScary-regular.ttf"
TEXT = "Choose your character (press 1/2/3/4)"



class ChooseCharacterScreen(Ninja, Viking, Cowboy, Pirate):
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.bg_color = BG_COLOR
        self.text_color = TEXT_COLOR
        self.text = TEXT
        self.ninja = Ninja()
        self.viking = Viking()
        self.cowboy = Cowboy()
        self.pirate = Pirate()

    def display_characters(self, screen):
        characters = [
            self.ninja,
            self.viking,
            self.cowboy,
            self.pirate
        ]
        
        add_pixel_x = 210
        cnt = 0

        for character in characters:
            character_image_not_scaled = pygame.image.load(
                os.path.join(character.jpg_path)
            ).convert() #convert creates a copy that will load faster on the screen

            character_image = pygame.transform.scale(character_image_not_scaled, character.image_size)
            character_image_rect = character_image.get_rect()

            character_image_rect.centerx = (100 + cnt * add_pixel_x)
            cnt = cnt + 1
            character_image_rect.centery = (WINDOW_HEIGHT // 2)

            screen.blit(
                character_image,
                character_image_rect
            )
            

    def display_character_info(self, index, screen):
        pygame.init()
        pygame.font.init()

        characters = [
            self.ninja,
            self.viking,
            self.cowboy,
            self.pirate
        ]

        font = pygame.font.Font(FONT_PATH, 50) # path to font; size in pixels

        if index % 4 == 0 :
            name = "ninja"
        elif index % 4 == 1:
            name = "viking"
        elif index % 4 == 2:
            name = "cowboy"
        else:
            name = "pirate"

        #display the name, hp, attack_damage, attack_speed, superpower_damage, superpower_cooldown
        hp = str(characters[index].hp)
        attack_damage = str(characters[index].attack_damage)
        attack_speed = str(characters[index].attack_speed)
        superpower_damage = str(characters[index].superpower_damage)
        superpower_cooldown = str(characters[index].superpower_cooldown)

        text = ("HP = " + hp + "\n"
        + "Attack Damage = " + attack_damage + "\n"
        + "Attack Speed = " + attack_speed + "\n"
        + "Super Power Damage = " + superpower_damage + "\n"
        + "Super Power Cooldown = " + superpower_cooldown)

        lines = [
    "HP = " + hp,
    "Attack Damage = " + attack_damage,
    "Attack Speed = " + attack_speed,
    "Super Power Damage = " + superpower_damage,
    "Super Power Cooldown = " + superpower_cooldown
]

        y_position = WINDOW_HEIGHT // 3  # Initial vertical position

        for line in lines:
            rendered_line = font.render(line, True, self.text_color, self.bg_color)
            text_rect = rendered_line.get_rect(centerx=WINDOW_WIDTH // 2, centery=y_position)
            screen.blit(rendered_line, text_rect)
            y_position += rendered_line.get_height()  # Adjust vertical position for the next line


        # rendered_text = font.render(
        #         text,
        #         True,
        #         self.text_color,
        #         self.bg_color
        # )

        # text_rect = rendered_text.get_rect()

        # text_rect.centerx = (
        #     WINDOW_WIDTH//2
        # )

        # text_rect.centery = (
        #     WINDOW_HEIGHT//1.3
        # )

        # screen.blit(
        #     rendered_text, 
        #     text_rect
        #     )
        


        ####### DISPLAY CHARACTER IMAGE #######
        character_image_not_scaled = pygame.image.load(
                os.path.join(characters[index].jpg_path)
            ).convert() #convert creates a copy that will load faster on the screen
        
        character_image = pygame.transform.scale(character_image_not_scaled, characters[index].image_size)
        character_image_rect = character_image.get_rect()
        character_image_rect.centerx = (WINDOW_WIDTH // 2)
        character_image_rect.centery = (WINDOW_HEIGHT // 6)

        screen.blit(
                character_image,
                character_image_rect
            )




    def display_the_screen(self):
        pygame.init()
        pygame.font.init()
        
        screen = self.screen
        screen.fill(self.bg_color)

        font = pygame.font.Font(FONT_PATH, 50) # path to font; size in pixels

        #null chars raise a typerror
        rendered_text = font.render(
                self.text,
                True,
                self.text_color,
                self.bg_color
        )

        text_rect = rendered_text.get_rect()

        text_rect.centerx = (
            WINDOW_WIDTH//2
        )

        text_rect.centery = (
            WINDOW_HEIGHT//1.3
        )
        
        screen.blit(
            rendered_text, 
            text_rect
            )

        # screen.blit(
        #     rendered_text,
        #     text_rect
        # )

        
        #display the ninja character
        self.display_characters(screen)

        # self.display_character_info(2, screen)

        pygame.display.flip() #update the screen
      
