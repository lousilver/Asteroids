import sys
import pygame
from constants import *
from player import Player
from logger import log_state,log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0

    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()

    Player.containers=(updatable,drawable)
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable,)
    Shot.containers=(shots,updatable,drawable)

    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    field=AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill((0,0,0))
        dt=clock.tick(60)/1000

        updatable.update(dt)
        for rock in asteroids:
            if player.detect_collision(rock):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if rock.detect_collision(shot):
                    log_event("asteroid_shot")
                    rock.split()
                    shot.kill()
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
