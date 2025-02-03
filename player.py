import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # To draw the player, overriding the draw method of CircleShape. It should take the screen object as a parameter, and call pygame.draw.polygon. It takes:
    # The screen object
    # A color ("white")
    # A list of points (self.triangle())
    # A line width (2) 
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # rotate method that will rotate the player by a certain amount. It should take the delta time as a parameter and increase the rotation attribute by PLAYER_TURN_SPEED * dt.    
    def rotate(self, dt):   
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # update method that will update the player's position.
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
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt