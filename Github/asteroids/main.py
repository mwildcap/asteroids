import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)
Player.containers = (updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)

field = AsteroidField()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0


    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(("black"))
        updatable.update(dt)
        for objects in asteroids: 
            if player.collision(objects) == True:
                print("Game over!")
                raise Exception(sys.exit())
            for bullet in shots:
                if bullet.collision(objects) == True:
                    objects.split()

        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
