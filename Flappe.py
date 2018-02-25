import sys
import pip

if __name__ == '__main__':
    try:
        import pygame
    except ModuleNotFoundError:
        pip.main('install pygame'.split())

    sys.path.insert(0, './src')
    import game

    pygame.init()
    game.title()
    pygame.quit()
    