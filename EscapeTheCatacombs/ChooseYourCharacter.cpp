#include "defs.h"



void chooseYourCharacter(static std::vector<Character> characters) {

	SDL_Window* window{};

	//Create window
	window = SDL_CreateWindow(
		"Choose your character",
		SDL_WINDOWPOS_CENTERED,
		SDL_WINDOWPOS_CENTERED,
		WINDOW_HEIGHT,
		WINDOW_WIDTH,
		0
	);

	//Renderer Window
	SDL_Renderer* renderer{SDL_CreateRenderer(window, -1, 0)};

	//Now we'll deal with the fonts

	if (TTF_Init() < 0) //init the font loader
		std::cout << "TTF init failed";

	TTF_Font* font{ TTF_OpenFont("C://Users//leona//OneDrive//Desktop//Escape The Catacombs//EscapeTheCatacombs//EscapeTheCatacombs//Fonts//ilits.ttf", 25) };
	if (!font) //test if font loads
		std::cout << "Font failed to load!\n";

		SDL_Color color{ RED };

		SDL_Surface* surfaceMessage = TTF_RenderText_Solid(font, "Choose your character", color);
		if (!surfaceMessage)
			std::cout << "Text failed to render\n";

		//covnert surfaceMessage into a texture
		SDL_Texture* message = SDL_CreateTextureFromSurface(renderer, surfaceMessage);

		//A SDL_Rect is a rectangular area of pixels
		SDL_Rect questionRectangle{
			(WINDOW_WIDTH - MENU_QUESTION_RECTANGLE_WIDTH) / 2, // Ox axis
			0, // Oy axis
			MENU_QUESTION_RECTANGLE_WIDTH,
			MENU_QUESTION_RECTANGLE_HEIGHT };


		//SDL_BlitSurface()
		SDL_RenderCopy(renderer, message, NULL, &questionRectangle);
		SDL_RenderPresent(renderer);
}