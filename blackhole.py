import pygame
import math

pygame.init()
WIDTH , HEIGHT = 800,600
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60

G = 6.67430e-11
C = 299792458

RED = (255,0,0)

class BlackHole:
    SCALE = 5e-9
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.position = [x,y]
        self.mass = mass
        self.r_s = 2 * G * mass / C**2
        self.radius = self.r_s * self.SCALE
        self.color = RED
    def draw(self,window):
        pygame.draw.circle(window, self.color, (int(self.position[0]),int(self.position[1])), int(self.radius))

def main(window):
    clock = pygame.time.Clock()
    running = True
    

    SagA = BlackHole(WIDTH-WIDTH/4,HEIGHT/2, 8.54e36)

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        SagA.draw(window)
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main(WINDOW)