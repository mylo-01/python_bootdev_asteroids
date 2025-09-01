import pygame
import random
from constants import *
from circle_shape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2 )

    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = a * 1.2
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = b * 1.2