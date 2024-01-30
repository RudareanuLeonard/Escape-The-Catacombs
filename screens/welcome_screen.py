from imports.import_libraries import *
from imports.import_files import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

BG_COLOR = "red"
TEXT_COLOR = "black"

FONT_PATH = "fonts/NoScary-regular.ttf"
TEXT = "Are you ready? Press Y to start..."

class WelcomeScreen:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.bg_color = BG_COLOR
        self.text_color = TEXT_COLOR
        self.text = TEXT


    def display_the_screen(self):

        pygame.init()
        pygame.font.init()

        screen = self.screen
        screen.fill(self.bg_color)

        font = pygame.font.Font(FONT_PATH, 72) # path to font; size in pixels
        # print("FONT = ", font)
        
        #null chars raise a typerror
        rendered_text = font.render(
                self.text,
                True,
                self.text_color,
                self.bg_color
        )

        text_rect = rendered_text.get_rect()

        text_rect.center = (
            WINDOW_WIDTH//2,
            WINDOW_HEIGHT//2
        )
        
        screen.blit(
            rendered_text, 
            text_rect
            )
        pygame.display.flip()
        # pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)).blit(rendered_text, text_rect)

