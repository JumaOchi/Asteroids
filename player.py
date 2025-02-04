import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape) :
    def __init__(self, x, y, radius) :
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shoot_cooldown = 0 #new variable to act as timer

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

