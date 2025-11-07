import pygame
from constants import *
from player import Player
from logger import log_state

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers(updatable,drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill((0,0,0))
        player.draw(screen)
        dt=clock.tick(60)/1000
        player.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
