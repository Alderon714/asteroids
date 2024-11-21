# create Player via CircleShape via Sprite in Pygame
import pygame
from circleshape import CircleShape
from constants import *

#NOTE: To create this and override stuff in CircleShape correctly you have to 
#       put all the functions inside of the "class" stuff ie. indent it all dummy! 
#       *Lesson learned*
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # draw the player on the screen overrideing CircleShape's draw method/function
    def draw(self, screen):
        # do something
        pygame.draw.polygon(screen, "red", self.triangle(), 2)

    # rotate it
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt # *rolls eyes* to update dummy it's a accumulate ie += not =

    # rotate actions
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # left turn Clyde
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # right turn Clyde
            self.rotate(dt)
        if keys[pygame.K_w]:
            # forward Clyde
            self.move(dt)
        if keys[pygame.K_s]:
            # backup Clyde
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
