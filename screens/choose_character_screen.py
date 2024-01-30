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
TEXT = "Choose your character"



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


    # def display_ninja(self,screen):
    #     # print(self.ninja.superpower_damage)
    #     ninja_image_not_scaled = pygame.image.load(
    #         os.path.join(self.ninja.jpg_path)
    #     ).convert() #convert creates a copy that will load faster on the screen

    #     ninja_image = pygame.transform.scale(ninja_image_not_scaled, self.ninja.image_size)
    #     ninja_image_rect = ninja_image.get_rect()

    #     ninja_image_rect.centerx = (WINDOW_WIDTH//2)
    #     ninja_image_rect.centery = (WINDOW_HEIGHT//2)


    #     screen.blit(
    #         ninja_image,
    #         ninja_image_rect
    #     )


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

        screen.blit(
            rendered_text,
            text_rect
        )

        
        #display the ninja character
        self.display_characters(screen)

        pygame.display.flip() #update the screen
      
