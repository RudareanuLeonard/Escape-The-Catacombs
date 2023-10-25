#include "defs.h"


void startMenu() {


	SDL_Window* window;

	window = SDL_CreateWindow(
		"Escape the catacombs",
		SDL_WINDOWPOS_CENTERED,
		SDL_WINDOWPOS_CENTERED,
		WINDOW_HEIGHT,
		WINDOW_WIDTH,
		0);

	SDL_Renderer* renderer{ SDL_CreateRenderer(window, -1, 0)};


	if (TTF_Init() < 0)
		std::cout << "TTF init failed";

	TTF_Font* font{ TTF_OpenFont("C://Users//leona//OneDrive//Desktop//Escape The Catacombs//EscapeTheCatacombs//EscapeTheCatacombs//Fonts//ilits.ttf", 25) };
	if (!font) {
	std::cout << "Failed to load font: " << TTF_GetError() << "\n";
	}
	SDL_Color color{ RED };

	SDL_Surface* surfaceMessage = TTF_RenderText_Solid(font, "Are you ready?", color);
	if (!surfaceMessage)
		std::cout << "Text failed to render\n";

	//covnert surfaceMessage into a texture
	SDL_Texture* message = SDL_CreateTextureFromSurface(renderer, surfaceMessage);

	//A SDL_Rect is a rectangular area of pixels
	SDL_Rect questionRectangle{ 
		(WINDOW_WIDTH - MENU_QUESTION_RECTANGLE_WIDTH) / 2, // Ox axis
		0, // Oy axis
		MENU_QUESTION_RECTANGLE_WIDTH, 
		MENU_QUESTION_RECTANGLE_HEIGHT};
	
	
	//SDL_BlitSurface()
	SDL_RenderCopy(renderer, message, NULL, &questionRectangle);
	

	TTF_Font* fontGoToNextLevel{TTF_OpenFont("C://Users//leona//OneDrive//Desktop//Escape The Catacombs//EscapeTheCatacombs//EscapeTheCatacombs//Fonts//FilthofIcarus-Regular.ttf", 25)};

	if (!fontGoToNextLevel)
		std::cout << "goToNextLevel font failed to load";

	SDL_Surface* goToNextLevelSurface = TTF_RenderText_Solid(fontGoToNextLevel, "Press Y to start", { RED });
	SDL_Texture* goToNextLevelMessage = SDL_CreateTextureFromSurface(renderer, goToNextLevelSurface);
	SDL_Rect goToNextLevelRectangle{
	(WINDOW_WIDTH - MENU_GO_TO_NEXT_LEVEL_RECTANGLE_WIDTH) / 2,
	(WINDOW_HEIGHT - MENU_GO_TO_NEXT_LEVEL_RECTANGLE_HEIGHT) / 2,
	MENU_GO_TO_NEXT_LEVEL_RECTANGLE_WIDTH,
	MENU_GO_TO_NEXT_LEVEL_RECTANGLE_HEIGHT
	};

	SDL_RenderCopy(renderer, goToNextLevelMessage, NULL, &goToNextLevelRectangle);
	
	SDL_RenderPresent(renderer);

	SDL_DestroyTexture(message);
	SDL_DestroyTexture(goToNextLevelMessage);
	SDL_FreeSurface(surfaceMessage);


}