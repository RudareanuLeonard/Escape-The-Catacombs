from imports.import_libraries import *
from imports.import_files import *

welcome_screen = WelcomeScreen()
choose_character_screen = ChooseCharacterScreen()



#####################################################################

# TEST WELCOME SCREEN HERE

####################################################################




########### IT WORKS - COMMENTED ONLY TO TEST OTHER THINGS #############

# pick_character_index = 0

# while welcome_screen.running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             welcome_screen.running = False
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
#             print(f"{event.key}PRESSED")
#             welcome_screen.running = False
#     welcome_screen.display_the_screen()

    
#     while choose_character_screen.running and welcome_screen.running == False:
#             print("B")
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     choose_character_screen.running = False
#                 choose_character_screen.display_the_screen()

#                 if event.type == pygame.KEYDOWN and (event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4):
#                     print(f"{event.key} PRESSED")
#                     if event.key == pygame.K_1:
#                         pick_character_index = 0
#                         choose_character_screen.running = False
#                     elif event.key == pygame.K_2:
#                         pick_character_index = 1
#                         choose_character_screen.running = False
#                     elif event.key == pygame.K_3:
#                         pick_character_index = 2
#                         choose_character_screen.running = False
#                     else:
#                         pick_character_index = 3
#                         choose_character_screen.running = False
#             # print(pick_character_index)
                    



#### TEST LVL 1 MAP ####

first_level_screen = FirstLevelScreen()

while first_level_screen.running:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    first_level_screen.running = False
    first_level_screen.display_the_screen()