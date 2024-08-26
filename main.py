import sys
import pygame

from constants import *     # Importing all variables from another file

# Pygame code
pygame.init()   # Initializing the pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))   #Display screen size
pygame.display.set_caption("TIC-TAC-TOE AI")    # Title display


# Main method
def main():
    
    while True:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit(
                sys.exit()
                )

main()