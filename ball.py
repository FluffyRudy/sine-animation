import pygame
import random
import math

class Ball(pygame.sprite.Sprite):
    size = 5
    increase_factor = 0.1
    hr_displacement = 5

    def __init__(self, parent_dim: pygame.Rect, init_vdir: int=1):
        super().__init__()
        self.parent_dim = parent_dim
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect(topleft=(0, parent_dim.centery))
        self.theta = 0
        self.init_vdir = init_vdir
        self.color = generate_random_color()
        self.amplitude = parent_dim.centery // 2

    def update(self, surface):
        pygame.draw.circle(self.image, self.color, (self.size//2, self.size//2), self.size//2)
        self.rect.x = int(self.rect.x  + self.hr_displacement)
        self.rect.y =  self.parent_dim.centery + int(math.sin(self.theta) * self.amplitude) * self.init_vdir
        self.theta = self.theta + self.increase_factor
        if self.theta >= 360:
            self.theta = 0
        if self.rect.x >= self.parent_dim.width:
            self.amplitude = self.parent_dim.centery // random.choice([2, 3, 4, 1])
            self.rect.x = -self.size
            self.color = generate_random_color()
            surface.fill("black")

def generate_random_color():
    return pygame.Color(random.choice(["red", "skyblue", "lime", "yellow", "pink", "white"]))
