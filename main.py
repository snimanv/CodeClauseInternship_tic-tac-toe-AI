import sys
import pygame

from constants import *     # Importing all variables from another file

# Pygame code
pygame.init()   # Initializing the pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))   #Display screen size
pygame.display.set_caption("TIC-TAC-TOE AI")    # Title display
screen.fill(BG_COLOUR)

class Game:

    def __init__(self):
        self.show_lines()

    def show_lines(self):
        # Vertical
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # Horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)


# Main method
def main():

    # Object
    game = Game()
    
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()


main()