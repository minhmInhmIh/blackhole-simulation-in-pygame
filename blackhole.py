import pygame
import math

pygame.init()
WIDTH , HEIGHT = 800,600
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60

G = 6.67430e-11
C = 299792458

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

SCALE = 5e-9

class BlackHole:
    
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.position = [x,y]
        self.mass = mass
        self.r_s = 2 * G * mass / C**2
        self.radius = self.r_s * SCALE
        self.color = RED
    def draw(self,window):
        pygame.draw.circle(window, self.color, (int(self.position[0]),int(self.position[1])), int(self.radius))


SagA = BlackHole(WIDTH/2,HEIGHT/2, 8.54e36)
class Ray:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        speed = 5
        self.vx = speed
        self.vy = 0
        self.trail = []
        self.alive = True

    
    def hit_blackhole(self, blackhole):
        dx = blackhole.x - self.x
        dy = blackhole.y - self.y
        dist = math.hypot(dx, dy)

        return dist <= blackhole.radius



    def draw(self, window):
        pygame.draw.circle(window, WHITE, (int(self.x), int(self.y)), 3)
        if len(self.trail) > 1:
            pygame.draw.lines(window, WHITE, False, self.trail, 2)
    def step(self, blackhole):
        # gravity
        dx = blackhole.x - self.x
        dy = blackhole.y - self.y
        dist = math.hypot(dx, dy)

        if dist != 0:
            dx /= dist
            dy /= dist
            force = 8000 / dist**2
            self.vx += dx * force
            self.vy += dy * force

        # predict next position
        next_x = self.x + self.vx
        next_y = self.y + self.vy

        next_dist = math.hypot(blackhole.x - next_x, blackhole.y - next_y)

        if next_dist <= blackhole.radius:
            # snap exactly to edge
            dx = next_x - blackhole.x
            dy = next_y - blackhole.y
            d = math.hypot(dx, dy)

            if d != 0:
                dx /= d
                dy /= d

                next_x = blackhole.x + dx * blackhole.radius
                next_y = blackhole.y + dy * blackhole.radius

            self.trail.append((next_x, next_y))
            self.x = next_x
            self.y = next_y

            return False  # stop ray

        # normal move
        self.x = next_x
        self.y = next_y
        self.trail.append((self.x, self.y))

        return True


def main(window):
    clock = pygame.time.Clock()
    running = True
    # rays = Ray(0, HEIGHT/2,SagA.x, SagA.y)
    # rays = Ray(0,300)
    number_of_rays = 50
    rays = []
    for i in range(0, HEIGHT, HEIGHT//number_of_rays):
        ray = Ray(0, i)
        rays.append(ray)

    while running:
        clock.tick(FPS)
        window.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        SagA.draw(window)

        for ray in rays:
            ray.draw(window)
            if ray.alive:
                ray.step(SagA)
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main(WINDOW)