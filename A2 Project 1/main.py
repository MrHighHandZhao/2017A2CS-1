import pygame
import sys
import traceback
import myplane
import bullet
import enemy
import supply
from pygame.locals import *
from random import *


pygame.init()
pygame.mixer.init()
bg_size = width, height = 480, 960
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Thunder-The Last War")
background = pygame.image.load("images/universe.png").convert()

def main():
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
    
