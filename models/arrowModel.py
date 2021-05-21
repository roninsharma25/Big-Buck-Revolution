# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
#
# arrowModel.py: a model of an arrow

from constants import *
import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, file, size, pos, speed = (0,0), 
                noteTime = 0, direction = 0, duration = 0, 
                bpm = 0, approachRate = 0, drain = 0):
        """
        file (string): file name
        size (tuple of length 2): x,y size dimensions
        pos (tuple of length 2): x,y initial positions
        speed (list of length 2): x,y speed update vector
        direction (int): 1 - left, 2 - down, 3 - up, 4 - right
        duration (float)
        noteTime (float)
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file)
        self.image = pygame.transform.scale(self.image, size)

        if (direction == 1):
            self.image = pygame.transform.rotate(self.image, 90)
        elif (direction == 2):
            self.image = pygame.transform.rotate(self.image, 180)
        elif (direction == 3):
            self.image = pygame.transform.rotate(self.image, 0)
        else: # direction = 4
            self.image = pygame.transform.rotate(self.image, 270)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
        self.direction = direction
        self.duration = duration
        self.noteTime = noteTime
        self.approachRate = approachRate
        self.drain = 0
        self.bpm = bpm
        self.distance = BOTTOM - self.rect.y

    def update(self, time, up = False):
        #self.rect.y = BOTTOM + (time - self.noteTime) * self.approachRate
        # Total distance = BOTTOM - startY
        # Velocity = distance / self.approachRate
        if up:
            self.rect.y = self.rect.y - (50 + BOTTOM / self.approachRate) / FPS
            #self.rect.y = self.rect.y - (self.distance / self.approachRate) / FPS
            # BOTTOM, 
        else:
            self.rect.y = self.rect.y + (self.distance / self.approachRate) / FPS

    def draw(self, view):
        view.blit(self.image, self.rect)
    
    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y
    
    def delete(self):
        self.rect.y = BOTTOM + 1000
        self.distance = 0
    
    def format(self):
        return [self.noteTime, self.direction - 1, self.duration]
