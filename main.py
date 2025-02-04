import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main() :
    pygame.init()

    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Creating two groups for the game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #Setting up player container
    Player.containers = (updatable, drawable)
    #Setting up asteroid container
    Asteroid.containers = (updatable, drawable, asteroids)
    #Setting up asteroid field container
    AsteroidField.containers = (updatable)
    time = pygame.time.Clock()
    dt = 0
    #Creating the player object
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    #Creating the asteroid field object
    asteroid_field = AsteroidField()
    # Set up a new group in your initialization code that contains all of your shots.
    shots_group = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots_group)

    #Main game loop
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        #Hook the update method into the game loop by calling it on the player object each frame before rendering
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)#drawing player on screen/ rendering
        #iterate over all of the objects in your asteroids group. 
        # Check if any of them collide with the player. If a collision
        #  is detected, the program should print Game over on screen! and immediately exit the program
        for asteroid in asteroids:
            if player1.collision(asteroid):
                print("Game over!")
                return
        pygame.display.flip()
        time.tick(60)
        dt = time.tick(60) / 1000.0
        

if __name__ == "__main__" :
    main()