from imports.import_libraries import *
from imports.import_files import *

welcome_screen = WelcomeScreen()
choose_character_screen = ChooseCharacterScreen()



#####################################################################

# TEST WELCOME SCREEN HERE

#####################################################################
# while welcome_screen.running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             welcome_screen.running = False
#     welcome_screen.display_the_screen()


while choose_character_screen.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            choose_character_screen.running = False
        choose_character_screen.display_the_screen()