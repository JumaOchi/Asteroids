import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main() :
    pygame.init()
    font = pygame.font.SysFont(None, 36)  # Default system font, size 36


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
                # Display Game Over at the center
                game_over_surface = font.render("Game Over!", True, (255, 0, 0))
                screen.blit(game_over_surface, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(2000)  # Pause for 2 seconds
                return  # Exit after showing Game Over

        #iterating to check if any of the shots collide with the asteroids
        for shot in shots_group:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    #print("Hit detected!")  # Debugging line
                    player1.add_score(asteroid)  # Add points based on asteroid size
                    asteroid.split()
        
        # Render score on the top-left corner
        score_surface = font.render(f"Score: {player1.score}", True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))


        pygame.display.flip()
        time.tick(60)
        dt = time.tick(60) / 1000.0
        

if __name__ == "__main__" :
    main()