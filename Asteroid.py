import random
from CircleShape import *
from Constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = None  # This will be set in the main game

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

        # Add self to containers if they exist
        if Asteroid.containers:
            for container in Asteroid.containers:
                container.add(self)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)

            new_asteroid_size = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_size)
            new_asteroid1.velocity = vector1 * 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_size)
            new_asteroid2.velocity = vector2 * 1.2

