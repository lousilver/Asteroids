from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self,dt):
        self.position+=(self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius<ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_radius=self.radius - ASTEROID_MIN_RADIUS
            asteroid1=Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2=Asteroid(self.position.x,self.position.y,new_radius)
            angle=random.uniform(20,50)
            asteroid1.velocity = self.velocity.rotate(angle)
            asteroid2.velocity = self.velocity.rotate(-angle)
