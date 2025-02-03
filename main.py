import pygame
from constants import *
from player import Player


def main() :
    pygame.init()

    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        #Hook the update method into the game loop by calling it on the player object each frame before rendering
        player1.update(dt)
        player1.draw(screen) #drawing player on screen/ rendering
        pygame.display.flip()
        time.tick(60)
        dt = time.tick(60) / 1000.0
        

if __name__ == "__main__" :
    main()