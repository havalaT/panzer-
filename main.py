import pygame
import sys
from random import randrange
import keyboard
import pygame.locals
import time

if __name__ == "__main__":
    screen = pygame.display.set_mode((500, 600))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        pygame.display.update()