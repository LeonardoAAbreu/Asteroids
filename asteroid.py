import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        astro_vector_right = self.velocity.rotate(random.uniform(20, 50))
        astro_vector_left = self.velocity.rotate(-random.uniform(20, 50))

        self.radius = self.radius - ASTEROID_MIN_RADIUS

        astro_right = Asteroid(self.position.x, self.position.y, self.radius)
        astro_left = Asteroid(self.position.x, self.position.y, self.radius)
        astro_right.velocity = astro_vector_right * 1.2
        astro_left.velocity = astro_vector_left * 1.2
