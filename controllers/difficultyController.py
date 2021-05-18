# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
# 
# menuController.py: a controller for the song select screen

from models.buttonModel import Button
from inputController import *
from constants import *
import pygame

class DifficultyController():
    """
    Menu Controller is a controller that handles updating and drawing the screen
    when the player is accessing and interacting with the main menu.
    """

    def __init__(self):
        """
        Instantiates a new menu
        """
        self.logo = pygame.image.load("assets/logo.png")
        if LARGE:
            self.buttons = [
                Button("Yes", (960, 700)),
                Button("No", (960, 950))
            ]
        else:
            self.buttons = [
                Button("Yes", (320, 300)),
                Button("No", (320, 400))
            ]

        self.exitCode = -1
        self.selected = 0
        self.buttons[self.selected].setSelected(True)
        self.should_exit = False
        self.flag = False
        self.song = 0
        self.mult = False
        self.font = pygame.font.Font(None, 40)
        self.bbbImages = []
        for file in BBB_IMAGES:
            img = pygame.transform.scale(pygame.image.load(file), BBB_IMAGE_SIZE)
            self.bbbImages.append(img)

    def start(self, song, mult = False):
        self.song = song
        self.mult = mult

    def update(self, input, dt):
        """
        Translates input actions into menu actions
        """
        self.exitCode = -1
        if input.pressed_back():
            self.should_exit = True
        elif input.pressed_right():
            self.buttons[self.selected].setHighlighted(True)
        elif input.released_right():
            self.buttons[self.selected].setHighlighted(False)
            if self.flag:
                self.exitCode = self.selected
        elif input.pressed_down() and not self.buttons[self.selected].highlighted:
            self.buttons[self.selected].setSelected(False)
            self.selected = min(self.selected + 1, len(self.buttons) - 1)
            self.buttons[self.selected].setSelected(True)
        elif input.pressed_up() and not self.buttons[self.selected].highlighted:
            self.buttons[self.selected].setSelected(False)
            self.selected = max(self.selected - 1, 0)
            self.buttons[self.selected].setSelected(True)
        
        self.flag = True

    def draw(self, view, dt):
        """
        Draws buttons to view
        """
        view.blit(self.logo, self.logo.get_rect())
        for button in self.buttons:
            button.draw(view, dt)

        for i in range(len(self.bbbImages)):
            view.blit(self.bbbImages[i], self.bbbImages[i].get_rect(center = BBB_IMAGE_POS[i]))
        
        text = self.font.render("???", True, WHITE)
        view.blit(text, text.get_rect(center = BBB_TEXT_POS))
