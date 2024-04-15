import pygame
import sys
from ball import Ball

class Animation:
    WIDTH = 800
    HEIGHT = 600
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.angle = 0.0
        self.time = 0.0
        self.clock = pygame.time.Clock()

        self.ballGroup = pygame.sprite.Group()
        self.ball1 = Ball(self.screen.get_rect(), 1)
        self.ball2 = Ball(self.screen.get_rect(), -1)
        self.ballGroup.add(self.ball1)
        self.ballGroup.add(self.ball2)

    def run(self):
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
            self.ballGroup.update(self.screen)
            self.ballGroup.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    animation = Animation()
    animation.run()
