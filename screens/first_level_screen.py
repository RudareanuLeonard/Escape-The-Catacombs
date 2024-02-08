from imports.import_libraries import *
from imports.import_files import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

BG_COLOR = "red"
TEXT_COLOR = "black"

FONT_PATH = "fonts/NoScary-regular.ttf"
TEXT = "Choose your character (press 1/2/3/4)"

MAP_PATH = "levels/level1/jpgs/map1.png"

class FirstLevelScreen():
    def __init__(self, jpg_path=MAP_PATH) -> None:
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.jpg_path = jpg_path

    def display_the_screen(self):
        pygame.init()
        
        screen = self.screen
        map_image = pygame.image.load(
            os.path.join(self.jpg_path)
        ).convert()

        map_image_rect = map_image.get_rect()
        
        screen.blit(
            map_image,
            map_image_rect
        )

        pygame.display.flip()