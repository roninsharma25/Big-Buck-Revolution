# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
#
# buttonModel.py: a model of a highlightable and selectable button

from constants import *
import pygame

class Button():
    """
    A model of a Button
    """
    
    def __init__(self, label, position):
        """
        Initializes a Button

        Parameters: 
        label is a str
        selected is a bool
        """
        font = pygame.font.Font(None, 40)
        self.text_highlighted = font.render(label, True, BLUE)
        self.text_normal = font.render(label, True, WHITE)
        self.text_rect = self.text_normal.get_rect(center=position)
        self.indicator_highlighted = pygame.image.load("assets/indicatorHighlighted.png")
        self.indicator_normal = pygame.image.load("assets/indicator.png")
        self.indicator_rect = self.indicator_normal.get_rect(center=\
                (self.text_rect.x - 64, position[1]))
        self.highlighted = False
        self.selected = False
        self.position = position

    def setHighlighted(self, highlighted):
        self.highlighted = highlighted

    def setSelected(self, selected):
        self.selected = selected

    def draw(self, view, dt):
        if self.highlighted:
            view.blit(self.text_highlighted, self.text_rect)
            view.blit(self.indicator_highlighted, self.indicator_rect)
        elif self.selected:
            view.blit(self.text_normal, self.text_rect)
            view.blit(self.indicator_normal, self.indicator_rect)
        else:
            view.blit(self.text_normal, self.text_rect)
    
    def updateText(self, label):
        font = pygame.font.Font(None, 40)
        self.text_highlighted = font.render(label, True, BLUE)
        self.text_normal = font.render(label, True, WHITE)
        self.text_rect = self.text_normal.get_rect(center=self.position)

