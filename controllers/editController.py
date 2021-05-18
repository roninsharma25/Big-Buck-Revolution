# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
# 
# menuController.py: a controller for the song select screen

from models.buttonModel import Button
from inputController import *
from gameController import *
from constants import *
import pygame
import json
import random

posDict = {0: (ARROW_LEFT[0], BOTTOM), 1: (ARROW_DOWN[0], BOTTOM), 2: (ARROW_UP[0], BOTTOM), 3: (ARROW_RIGHT[0], BOTTOM)}
MAXTIME = 5

class EditController():
    """
    Menu Controller is a controller that handles updating and drawing the screen
    when the player is accessing and interacting with the main menu.
    """

    def __init__(self):
        """
        Instantiates a new menu
        """
        self.logo = pygame.image.load("assets/logo.png")
        self.exitCode = -1
        self.selected = 0
        self.should_exit = False
        self.flag = False
        self.stationaryArrows = createArrows("", "assets/arrow.png", (50, 50), flag = True)
        self.pressedArrows = createArrows("", "assets/arrow_outline.png", (50, 50), flag = True)
        self.pressedArrowsDisplay = [False, False, False, False]
        self.fileName = "jsons/doitagain.json"
        self.newLevel = "jsons/createdLevel.json"

    def start(self, index, bbb):
        self.startTime = time.time()
        self.currentTime = time.time()
        self.elapsedTime = self.currentTime - self.startTime
        self.movingArrows = []
        self.done = False
        self.bbb = bbb

        pygame.mixer.init()
        json = SONGS[index][1]
        self.index = index
        self.fileName = parseSong("jsons/" + json)[1]
        playMusic(self.fileName, pygame.mixer)

    def update(self, input, dt):
        """
        Translates input actions into menu actions
        """
        self.currentTime = time.time()
        self.elapsedTime = self.currentTime - self.startTime

        if input.pressed_left():
            self.pressedArrowsDisplay[0] = True
            arrow = Arrow("assets/arrow.png", (50, 50), posDict[0], noteTime = self.elapsedTime, 
                    direction = 1, bpm = 120, approachRate = 0.5)
            self.movingArrows.append(arrow)
        elif input.released_left():
            self.pressedArrowsDisplay[0] = False

        if input.pressed_down():
            self.pressedArrowsDisplay[1] = True
            arrow = Arrow("assets/arrow.png", (50, 50), posDict[1], noteTime = self.elapsedTime, 
                    direction = 2, bpm = 120, approachRate = 0.5)
            self.movingArrows.append(arrow)
        elif input.released_down():
            self.pressedArrowsDisplay[1] = False

        if input.pressed_up():
            self.pressedArrowsDisplay[2] = True
            arrow = Arrow("assets/arrow.png", (50, 50), posDict[2], noteTime = self.elapsedTime, 
                    direction = 3, bpm = 120, approachRate = 0.5)
            self.movingArrows.append(arrow)
        elif input.released_up():
            self.pressedArrowsDisplay[2] = False

        if input.pressed_right():
            self.pressedArrowsDisplay[3] = True
            arrow = Arrow("assets/arrow.png", (50, 50), posDict[3], noteTime = self.elapsedTime, 
                    direction = 4, bpm = 120, approachRate = 0.5)
            self.movingArrows.append(arrow)
        elif input.released_right():
            self.pressedArrowsDisplay[3] = False
        
        if self.elapsedTime > MAXTIME:
            self.done = True

            # Save json
            jsons = [js[1] for js in SONGS]
            with open("jsons/" + random.choice(jsons)) as f:
                data = json.load(f)

            data["arrows"] = [arrow.format() for arrow in self.movingArrows]
            print(data)
            with open("jsons/createdLevel.json", "w") as f:
                json.dump(data, f)

            self.newLevel = "createdLevel.json"

    def draw(self, view, dt):
        """
        Draws buttons to view
        """
        view.blit(self.logo, self.logo.get_rect())
        for button in self.stationaryArrows:
            button.draw(view)

        for arrow in self.movingArrows:
            arrow.update(self.elapsedTime, True)
            arrow.draw(view)

        count = 0
        for arrow in self.pressedArrows:
            if self.pressedArrowsDisplay[count]:
                arrow.draw(view)
            count += 1
            