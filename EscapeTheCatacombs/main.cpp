#include "defs.h"

static int cnt{0};
int running{ 1 };
int main() {

	/*
	while (1) {
		startMenu();
		SDL_Delay(20000);

	}
	*/

	SDL_Event listenToKeyPressMenu;

	while (running) {
		std::cout << "cnt = " << cnt;
		startMenu();
		SDL_Delay(1000);
	/*	if (!SDL_PollEvent(&listenToKeyPressMenu))
			break;
	*/
		while (SDL_PollEvent(&listenToKeyPressMenu))
			if (listenToKeyPressMenu.key.keysym.sym == SDLK_y) {
				std::cout << "Y pressed";
				running = 0;
				break;
			}
				
	}




	return 0;
}