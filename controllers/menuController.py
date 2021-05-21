# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
# 
# menuController.py: a controller for the menu screen

from models.buttonModel import Button
from inputController import *
import pygame

class MenuController():
    """
    Menu Controller is a controller that handles updating and drawing the screen
    when the player is accessing and interacting with the main menu.
    """

    EXIT_SINGLEPLAYER = 0
    EXIT_MULTIPLAYER = 1
    EXIT_LEVELEDITOR = 2

    def __init__(self):
        """
        Instantiates a new menu
        """
        self.logo = pygame.image.load("assets/logo.png")

        if LARGE:
            self.buttons = [
                Button("Single Player", (960, 450)),
                Button("Multiplayer", (960, 600)),
                Button("Level Editor", (960, 750))
            ]
        else:
            self.buttons = [
                Button("Single Player", (320, 200)),
                Button("Multiplayer", (320, 300)),
                Button("Level Editor", (320, 400))
            ]
        
        self.exitCode = -1
        self.selected = 0
        self.buttons[self.selected].setSelected(True)

    def update(self, input, dt):
        """
        Translates input actions into menu actions
        """
        self.exitCode = -1
        if input.pressed_back():
            InputController.should_quit = True
        elif input.pressed_right():
            self.buttons[self.selected].setHighlighted(True)
        elif input.released_right():
            self.buttons[self.selected].setHighlighted(False)
            self.exitCode = self.selected
        elif input.pressed_down() and not self.buttons[self.selected].highlighted:
            self.buttons[self.selected].setSelected(False)
            self.selected = min(self.selected + 1, len(self.buttons) - 1)
            self.buttons[self.selected].setSelected(True)
        elif input.pressed_up() and not self.buttons[self.selected].highlighted:
            self.buttons[self.selected].setSelected(False)
            self.selected = max(self.selected - 1, 0)
            self.buttons[self.selected].setSelected(True)

    def draw(self, view, dt):
        """
        Draws buttons to view
        """
        view.blit(self.logo, self.logo.get_rect())
        for button in self.buttons:
            button.draw(view, dt)

