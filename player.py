import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape) :
    def __init__(self, x, y, radius) :
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shoot_cooldown = 0 #new variable to act as timer
        self.score = 0
        self.is_alive = True  # Track player state

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    #Overrides the draw method from the CircleShape class
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)


    def rotate(self, dt) :
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            #prevents the player from shooting again until the cooldown is
            if self.shoot_cooldown <= 0:
                self.shoot()
                self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        #decrements the cooldown timer
        self.shoot_cooldown -= dt

    def move(self, dt) :
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        position = self.position + forward * self.radius
        shot = Shot(position.x, position.y, SHOT_RADIUS)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

    def add_score(self, asteroid):
        if asteroid.radius <= SMALL_ASTEROID_RADIUS:
            self.score += 3
        elif asteroid.radius <= MEDIUM_ASTEROID_RADIUS:
            self.score += 2
        else:
            self.score += 1

    def hit(self):
        self.is_alive = False  # Mark player as dead
    