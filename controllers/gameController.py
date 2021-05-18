# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
# 
# gameController.py: a controller for the game screen

from constants import *
from models.arrowModel import Arrow
import pygame
import time
import json

TIME_DELAY = 1
SCORE_BUTTON = (0, 0)

fileStart = "assets/BBB/frame_"
fileEnd = "_delay-0.07s.png"

class GameController():
    """
    Game Controller is a controller that handles updating and drawing the screen
    when the player is accessing and interacting with the main game.
    """

    def __init__(self):
        """
        Instantiates a new game
        """
        # Time attributes
        self.startTime = 0
        self.currentTime = 0
        self.elapsedTime = self.currentTime - self.startTime
        self.stationaryArrows = None
        self.arrows = None
        self.correct = False
        self.timeOffset = 0
        self.extraTime = 10 # Number of seconds the game window will remain aften the song ends

        # Game objects
        self.song = None

        # Multiplayer
        self.anotherGame = False

    def start(self, index, BBB = False, newLevel = (False, "createdLevel.json"), anotherGame = False):
        """
        Starts the game
        """
        pygame.mixer.init()

        if newLevel[0]:
            json = newLevel[1]
        else:
            json = SONGS[index][1]
        print(json)
        self.song, self.fileName, self.approachRate, self.drain, self.bpm = parseSong("jsons/" + json)
        self.stationaryArrows = createArrows(self.song, "assets/arrow.png", (50, 50), True)
        self.pressedArrows = createArrows(self.song, "assets/arrow_outline.png", (50, 50), True)
        self.pressedArrowsDisplay = [False, False, False, False]
        self.arrows = createArrows(self.song, "assets/arrow.png", (50, 50), approachRate = self.approachRate,
                                    drain = self.drain, bpm = self.bpm)
        playMusic(self.fileName, pygame.mixer)

        self.startTime = time.time()
        self.currentTime = time.time()
        self.elapsedTime = self.currentTime - self.startTime
        self.correct = False
        self.timeOffset = 0
        
        # Give more time after if there is a second player
        if (anotherGame):
            self.extraTime = 5 #15
        else:
            self.extraTime = 2 #10

        # Start and end indicies for active arrows
        self.startIndex = 0
        self.endIndex = 0

        # Score
        self.font = pygame.font.Font(None, 40)
        self.score = 0
        self.multiplier = 1

        # Multiplayer
        self.anotherGame = anotherGame

        # Exit
        self.should_exit = False

        # BBB
        if (BBB):
            self.BBB = True
            self.bbbCounter = 0
            self.bbbImages = []
            for i in range(30):
                img = pygame.transform.scale(pygame.image.load(fileStart + "{:02d}".format(i) + fileEnd), SIZE)
                self.bbbImages.append(img)
        else:
            self.BBB = False
        
        # Done
        self.lastArrowTime = self.song[-1][0] # absolute time of the last arrow
        self.done = False


    def update(self, input, dt):
        """
        Translates input actions into menu actions
        """
        self.currentTime = time.time()
        self.elapsedTime = self.currentTime - self.startTime

        if self.endIndex < len(self.arrows):
            nextArrow = self.arrows[self.endIndex]
            if (nextArrow.noteTime - self.elapsedTime <= nextArrow.approachRate):
                self.endIndex += 1
        self.endIndex = min(self.endIndex, len(self.arrows))

        if input.pressed_left():
            self.pressedArrowsDisplay[0] = True
            input.lightButton("left", self.checkPlayerInput(1))
        elif input.released_left():
            self.pressedArrowsDisplay[0] = False
            input.lightButton("left", "off")

        if input.pressed_down():
            self.pressedArrowsDisplay[1] = True
            input.lightButton("down", self.checkPlayerInput(2))
        elif input.released_down():
            self.pressedArrowsDisplay[1] = False
            input.lightButton("down", "off")

        if input.pressed_up():
            self.pressedArrowsDisplay[2] = True
            input.lightButton("up", self.checkPlayerInput(3))
        elif input.released_up():
            self.pressedArrowsDisplay[2] = False
            input.lightButton("up", "off")

        if input.pressed_right():
            self.pressedArrowsDisplay[3] = True
            input.lightButton("right", self.checkPlayerInput(4))
        elif input.released_right():
            self.pressedArrowsDisplay[3] = False
            input.lightButton("right", "off")
        
        if input.pressed_back():
            self.should_exit = True
            pygame.mixer.music.stop()
        
        input.lightButton("rim", COLORS[int(self.multiplier) % len(COLORS)])
        if (self.BBB):
            self.bbbCounter += 1
            self.bbbCounter %= len(self.bbbImages)

        # CORRECT
        if (self.correct):
            for arrow in self.arrows:
                arrow.noteTime += self.timeOffset
            self.correct = False
            self.timeOffset = 0
            print("CHANGED")

        # End game
        if self.elapsedTime > self.lastArrowTime + self.extraTime:
            self.done = True
            pygame.mixer.music.stop()

    def draw(self, view, dt):
        """
        Draws game objects to view
        """

        if (self.BBB):
            # Draw BBB
            img = self.bbbImages[self.bbbCounter]
            view.blit(img, img.get_rect())

        for arrow in self.stationaryArrows:
            arrow.draw(view)

        count = 0
        for arrow in self.arrows[self.startIndex:self.endIndex]:
            arrow.update(self.elapsedTime)
            arrow.draw(view)
            count += 1

            # CORRECT
            if (abs(arrow.getY() - BOTTOM) <= OFFSET):
                self.timeOffset = arrow.noteTime - self.elapsedTime
                if (abs(self.timeOffset) > 1): # Correct if notes are 1 second off
                    self.correct = True
                    print("CHANGE")

        count = 0
        for arrow in self.pressedArrows:
            if self.pressedArrowsDisplay[count]:
                arrow.draw(view)
            count += 1
        
        # Update score
        score_text = "Score: " + str(self.score)
        score_button = self.font.render(score_text, True, WHITE)
        score_rect = score_button.get_rect(topleft = SCORE_BUTTON)
        view.blit(score_button, score_rect)
        
    def checkPlayerInput(self, dir):
        """
        Update game state based on user input
        dir (int): 1 - left, 2 - down, 3 - up, 4 - right
        """
        arrow = self.closestArrow(dir)
        
        if (arrow is None): # pressed when there wasn't an arrow or arrow is below the bottom
            print("MISSED")
            return "white"
        else:
            print(abs(arrow.getY() - BOTTOM))
            if (abs(arrow.getY() - BOTTOM) <= OFFSET):
                print("HIT")
                self.score += self.multiplier * HIT_INCREMENT
                self.multiplier += 0.5
                arrow.delete()
                return "green"
            elif (abs(arrow.getY() - BOTTOM) <= OFFSET*2):
                print("ALMOST")
                self.score += self.multiplier * ALMOST_INCREMENT
                self.multiplier += 0.25
                arrow.delete()
                return "blue"
            else:
                print("MISSED")
                self.score -= MISSED
                self.multiplier = 1
                arrow.delete()
                return "red"
            

    def closestArrow(self, dir):
        """
        Returns the closest arrow above the bottom
        """
        closestY = SIZE[1]
        closestArrow = None
        for arrow in self.arrows[self.startIndex:self.endIndex]:
            yPos = arrow.getY()
            if (arrow.direction == dir and yPos <= (BOTTOM + OFFSET) and (BOTTOM + OFFSET - yPos <= closestY)):
                closestY = BOTTOM - yPos
                closestArrow = arrow
        
        return closestArrow


def createArrows(song, file, size, flag = False, bpm = 60, approachRate = 0, drain = 0):
    # For each entry in the list, (Arrow object, time)
    allArrows = [] 
    posDict = {0: ARROW_LEFT, 1: ARROW_DOWN, 2: ARROW_UP, 3: ARROW_RIGHT}
    if (not flag): # non-stationary arrows
        for entry in song:
            arrow = Arrow(file, size, posDict[entry[1]], [0, 2], entry[0], 
                            entry[1] + 1, entry[2], bpm, approachRate, drain)
            allArrows.append(arrow)
    else:
        for i in range(4):
            arrow = Arrow(file, size, (posDict[i][0], BOTTOM), direction = i + 1)
            allArrows.append(arrow)
    return allArrows

def playMusic(file, mixer):
    mixer.music.load(file)
    mixer.music.play()
    print("Started Music")

def parseSong(f1):
    with open(f1) as f:
        data = json.load(f)
    
    file = data["file"]
    bpm = data["BPM"]
    startTime = data["startTime"]
    approachRate = data["approachRate"]
    drain = data["drain"]
    arrows = data["arrows"]

    # Time (should overlap at bottom), direction, duration
    #[(1, 0, 0), (3, 1, 0), (4, 2, 0), (5, 3, 0)]
    rtArrows = [] 
    for arrow in arrows:
        rtArrows.append((startTime + (60/bpm) * arrow[0], arrow[1], arrow[2] * (60/bpm)))
    return rtArrows, file, approachRate, drain, bpm
