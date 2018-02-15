import pygame
import sys

sys.path.insert(0, './data/')
import game

if __name__ == '__main__':
	pygame.init()
	game.main()
	pygame.quit()